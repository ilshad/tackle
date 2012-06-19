# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.component import adapts
from zope.interface import implements
from zope.securitypolicy.interfaces import Allow, Unset
from zope.securitypolicy.interfaces import IPrincipalRoleManager
from zope.securitypolicy.interfaces import IPrincipalRoleMap
from zope.securitypolicy.interfaces import IPrincipalPermissionMap
from zope.security.interfaces import IPrincipal

from rwproperty import getproperty, setproperty

from tackle.interfaces import ISecuritySettings

class SecuritySettings(object):
    implements(ISecuritySettings)

    def __init__(self, context, principal_id):
        self.context = context
        self.principal_id = principal_id

    @getproperty
    def roles(self):
        prmap = IPrincipalRoleMap(self.context)
        return [ids for ids, setting in prmap.getRolesForPrincipal(self.principal_id)]

    @setproperty
    def roles(self, values):
        prmanager = IPrincipalRoleManager(self.context)
        for role_id in self.roles:
            prmanager.unsetRoleForPrincipal(role_id, self.principal_id)
        for role_id in values:
            prmanager.assignRoleToPrincipal(role_id, self.principal_id)

class UserPrincipalRoleMap(object):
    implements(IPrincipalRoleMap)
    adapts(IPrincipal)

    def __init__(self, principal):
        self.principal = principal

    def getPrincipalsForRole(self, role_id):
        return []

    def getRolesForPrincipal(self, principal_id):
        if principal_id == self.principal.id:
            return [('tackle.Owner', Allow)]
        return []

    def getSetting(self, role_id, principal_id):
        return Unset
 
    def getPrincipalsAndRoles(self):
        return []

class UserPrincipalPermissionMap(object):
    implements(IPrincipalPermissionMap)
    adapts(IPrincipal)

    def __init__(self, principal):
        self.principal = principal

    def getPrincipalsForPermission(self, permission_id):
        return []

    def getPermissionsForPrincipal(self, principal_id):
        return []

    def getSetting(self, permission_id, principal_id, default=Unset):
        if permission_id == 'tackle.UpdatePassword':
            if principal_id == self.principal.id:
                return Allow
        return default

    def getPrincipalsAndPermissions(self):
        return []
