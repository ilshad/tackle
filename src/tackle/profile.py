# 2010 Ilshad Khabibullin <astoon@spacta.com>

from rwproperty import getproperty, setproperty

from zope.interface import implements
from zope.component import adapts, getUtility
from zope.authentication.interfaces import IAuthentication
from zope.security.interfaces import IPrincipal
from zope.annotation import IAnnotations

from tackle.interfaces import IPrincipalProfileType, IBasicProfile
from tackle.util import internal_principal

def get_profile(principal_id, iface_type_name):
    iface = getUtility(IPrincipalProfileType, iface_type_name)
    auth = getUtility(IAuthentication)
    principal = auth.getPrincipal(principal_id)
    return iface(principal)

class BasicProfile(object):

    implements(IBasicProfile)
    adapts(IPrincipal)

    def __init__(self, principal):
        self.annotations = IAnnotations(principal)
        self.principal = principal

    @setproperty
    def name(self, v):
        self.annotations['name'] = v

        # for principalfolder search
        ip = internal_principal(self.principal.id)
        ip.title = v

    @getproperty
    def name(self):
        return self.annotations.get('name', self.principal.title)

    @setproperty
    def email(self, v):
        self.annotations['email'] = v

    @getproperty
    def email(self):
        return self.annotations.get('email', u'')
