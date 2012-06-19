# 2010 Ilshad Khabibullin <astoon@spacta.com>

from z3c.formui import form
from z3c.form import field, button
from zope.component import hooks
from zope.traversing.browser.absoluteurl import absoluteURL

from tackle.interfaces import IGroupParticipationPrincipal

class Pagelet(form.EditForm):

    fields = field.Fields(IGroupParticipationPrincipal)

    @button.buttonAndHandler(u'Back')
    def handleBack(self, action):
        self.request.response.redirect(
            u"%s/users" % absoluteURL(hooks.getSiteManager(), self.request))

    @button.buttonAndHandler(u'Apply')
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        changes = self.applyChanges(data)
        if changes:
            self.status = self.successMessage
        else:
            self.status = self.noChangesMessage
