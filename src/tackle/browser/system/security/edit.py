# 2010 Ilshad Khabibullin <astoon@spacta.com>

import urllib

from z3c.formui import form
from z3c.form import field, button

from zope.traversing.browser.absoluteurl import absoluteURL
from zope.authentication.interfaces import IAuthentication
from zope.dublincore.interfaces import IZopeDublinCore
from zope.component import getUtility, hooks
from zope.component.interfaces import ISite

from tackle.interfaces import ISecuritySettings

class Pagelet(form.EditForm):

    fields = field.Fields(ISecuritySettings)

    @button.buttonAndHandler(u'Back', name='back')
    def handleBack(self, action):
        context = self.context.context
        quote = lambda x:urllib.quote(x.encode("utf-8"))
        self.request.response.redirect(
            u"%s/select_group?context=%s&title=%s" % (
                absoluteURL(hooks.getSiteManager(), self.request),
                absoluteURL(context, self.request),
                quote(IZopeDublinCore(context).title or context.__name__)))

    @button.buttonAndHandler(u'Apply', name='apply')
    def handleApply(self, action):
        data, errors = self.extractData()
        self.status = errors and self.formErrorsMessage or (
            self.applyChanges(data) and
            self.successMessage or
            self.noChangesMessage)

    def get_principal_title(self):
        auth = getUtility(IAuthentication)
        principal = auth.getPrincipal(self.context.principal_id)
        return principal.title

    def get_context_name(self):
        c = self.context.context
        dc = IZopeDublinCore(c)
        name = ISite.providedBy(c) and u"SITE" or c.__name__
        return u"%s (%s)" % (name, dc.title)
