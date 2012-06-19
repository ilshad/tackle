# 2010 Ilshad Khabibullin <astoon@spacta.com>

from z3c.formui import form
from z3c.form import button
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.component.hooks import getSiteManager

class Pagelet(form.Form):

    @button.buttonAndHandler(u"Delete", name="delete")
    def handleDelete(self, action):
        name = self.request.get('id')
        del self.context[name]
        url = u"%s/groups" % absoluteURL(getSiteManager(), self.request)
        self.request.response.redirect(url)

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handleCancel(self, action):
        name = self.request.get('id')
        url = u"%s/%s/edit" % (absoluteURL(self.context, self.request), name)
        self.request.response.redirect(url)
