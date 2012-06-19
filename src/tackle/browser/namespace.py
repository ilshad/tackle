# 2010 Ilshad Khabibullin, <astoon@spacta.com>

from zope.location import LocationProxy
from zope.traversing.namespace import SimpleHandler
from zope.authentication.interfaces import IAuthentication
from zope.component import getUtility

from tackle.security import SecuritySettings

class security(SimpleHandler):

    def traverse(self, name, ignored):
        return LocationProxy(SecuritySettings(self.context, name),
                             self.context, '++security++%s' % name)

class user(SimpleHandler):

    def traverse(self, name, ignored):
        auth = getUtility(IAuthentication)
        return LocationProxy(auth.getPrincipal(name),
                             self.context, '++user++%s' % name)
