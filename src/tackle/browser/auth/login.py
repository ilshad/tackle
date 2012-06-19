# Copyright (C) Zope Corporation and Contributors.
# 2010 Ilshad Khabibullin, <astoon@spacta.com>

from zope import interface, component
from zope.app.publisher.interfaces.http import ILogin
from zope.authentication.interfaces import IUnauthenticatedPrincipal
from zope.authentication.interfaces import IAuthentication
from zope.app.pagetemplate import ViewPageTemplateFile

class Pagelet(object):
    interface.implements(ILogin)

    confirmation = ViewPageTemplateFile('login.pt')
    failed = ViewPageTemplateFile('login_failed.pt')

    def render(self):
        nextURL = self.request.get('nextURL')
        if IUnauthenticatedPrincipal(self.request.principal, False):
            component.getUtility(IAuthentication).unauthorized(
                self.request.principal.id, self.request)
            return self.failed()
        if nextURL is None:
            return self.confirmation()
        self.request.response.redirect(nextURL)
