# Copyright (C) Zope Corporation and Contributors.
# 2010 Ilshad Khabibullin, <astoon@spacta.com>

from zope import interface, component
from zope.authentication.interfaces import IUnauthenticatedPrincipal
from zope.authentication.interfaces import IAuthentication, ILogout
from zope.app.pagetemplate import ViewPageTemplateFile

class Pagelet(object):
    interface.implements(ILogout)

    confirmation = ViewPageTemplateFile('logout.pt')
    redirect = ViewPageTemplateFile('redirect.pt')

    def render(self):
        nextURL = self.request.get('nextURL')
        if not IUnauthenticatedPrincipal(self.request.principal, False):
            auth = component.getUtility(IAuthentication)
            ILogout(auth).logout(self.request)
            if nextURL:
                return self.redirect()
        if nextURL is None:
            return self.confirmation()
        return self.request.response.redirect(nextURL)
