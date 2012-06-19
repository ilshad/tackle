# 2010 Ilshad Khabibullin <astoon@spacta.com>

from persistent import Persistent
from BTrees.OOBTree import OOTreeSet

from zope.component import adapts
from zope.interface import implements
from zope.annotation import factory

from tackle.interfaces import ISubscription, ISubscribable
from tackle.profile import get_profile
from tackle.smtp import send_mail

class Subscription(Persistent):
    implements(ISubscription)
    adapts(ISubscribable)

    def __init__(self):
        self.subscribers = OOTreeSet()

    def subscribe(self, principal_id):
        self.subscribers.insert(principal_id)

    def unsubscribe(self, principal_id):
        self.subscribers.remove(principal_id)

    def send(self, message, subject):
        for pid in self.subscribers.keys():
            profile = get_profile(pid, "basic")
            send_mail(message, subject, profile.email)

annotation_factory = factory(Subscription)

def subscribe(ob, event):
    subscription = ISubscription(event.context)
    subscription.send(event.message)
