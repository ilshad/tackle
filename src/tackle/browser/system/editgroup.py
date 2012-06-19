# 2010 Ilshad Khabibullin <astoon@spacta.com>

from z3c.formui import form
from z3c.form import field, button
from zope.component import hooks
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.app.authentication.groupfolder import IGroupInformation

class Pagelet(form.EditForm):

    fields = field.Fields(IGroupInformation).select(
        'title', 'description')

    @button.buttonAndHandler(u'Back')
    def handleBack(self, action):
        self.request.response.redirect(
            u"%s/groups" % absoluteURL(hooks.getSiteManager(), self.request))

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

    @button.buttonAndHandler(u'Delete')
    def handleDelete(self, action):
        self.request.response.redirect(
            u"%s/delete?id=%s" % (
                absoluteURL(self.context.__parent__, self.request),
                self.context.__name__))
