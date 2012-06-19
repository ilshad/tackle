# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.interface import implements
from zope.component import getUtility, adapts
from zope.authentication.interfaces import IAuthentication
from zope.app.authentication import principalfolder
from rwproperty import setproperty, getproperty
from interfaces import IGroupParticipationPrincipal

class GroupParticipationPrincipal(object):

    implements(IGroupParticipationPrincipal)
    adapts(principalfolder.InternalPrincipal)

    def __init__(self, context):
        self.context = context
        auth = getUtility(IAuthentication)
        self.groupfolder = auth[u'groupfolder']
        self.principal_id = context.__parent__.prefix + context.__name__

    @setproperty
    def groups(self, v):
        if v is not None:
            l = v[:]
            for name in self.groupfolder.getGroupsForPrincipal(self.principal_id):
                k = name[len(self.groupfolder.prefix):]
                group = self.groupfolder[k]
                if k not in l:
                    pp = list(group.principals)
                    pp.remove(self.principal_id)                    
                    group.setPrincipals(pp)
                else:
                    l.remove(k)
            for k in l:
                group = self.groupfolder[k]
                pp = list(group.principals)
                pp.append(self.principal_id)                    
                group.setPrincipals(pp)

    @getproperty
    def groups(self):
        result = {}
        for name in self.groupfolder.getGroupsForPrincipal(self.principal_id):
            k = name[len(self.groupfolder.prefix):]
            result[k] = self.groupfolder[k]
        return result
