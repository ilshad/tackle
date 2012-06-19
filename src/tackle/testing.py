# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.interface import implements
from zope.sendmail.interfaces import IMailDelivery

class FakeMailDelivery(object):
    implements(IMailDelivery)

    def send(self, source, dest, body):
        print "*** Sending email from %s to %s:" % (source, dest)
        print body
        return 'fake-message-id@example.com'
