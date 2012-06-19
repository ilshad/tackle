# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.interface import implements

from tackle.interfaces import INewLocalSite
from tackle.interfaces import ISubscriptionEvent
from tackle.interfaces import IPasswordResetRequest
from tackle.interfaces import IPasswordResetEvent

class NewLocalSite(object):
    implements(INewLocalSite)

    def __init__(self, manager):
        self.manager = manager

class SubscriptionEvent(object):
    implements(ISubscriptionEvent)

    def __init__(self, context, message):
        self.context = context
        self.message = message

class PasswordResetRequest(object):
    implements(IPasswordResetRequest)

    def __init__(self, principal_id, login, code, req):
        self.principal_id = principal_id
        self.login = login
        self.code = code
        self.req = req

class PasswordResetEvent(object):
    implements(IPasswordResetEvent)

    def __init__(self, principal_id, password):
        self.principal_id = principal_id
        self.password = password
