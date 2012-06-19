# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.component import getUtility
from zope.securitypolicy.interfaces import IRole

class DisplayRolesForContext:

    def __call__(self):
        return u", ".join(
            getUtility(IRole, name=x).title
            for x in self.context.roles)
