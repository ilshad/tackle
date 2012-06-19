# 2010 Ilshad Khabibullin, <astoon@spacta.com>

from z3c.form import form, field, button
from zope.browserpage import ViewPageTemplateFile
from zope.component.interfaces import IFactory
from zope.dublincore.interfaces import IZopeDublinCore
from zope.lifecycleevent import ObjectCreatedEvent
from zope.lifecycleevent import ObjectModifiedEvent
from zope.security.proxy import getObject
from zope.component import getUtility
from zope.event import notify

from tackle.interfaces import IAddContent, IInstalledContent

class AddContent(form.Form):

    template = ViewPageTemplateFile("add.pt")
    fields = field.Fields(IAddContent)

    ignoreContext = True
    ignoreReadonly = True

    @button.buttonAndHandler(u"Add", name="add")
    def handleAdd(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        factory = getUtility(IFactory, name=data['factory'])
        ob = factory()
        title = data.get('title')
        if title:
            dc = IZopeDublinCore(ob)
            dc.title = title
        notify(ObjectCreatedEvent(ob))
        name = data['name']
        if name not in self.context:
            self.context[name] = ob
        else:
            self.status = u"Identifier already used"
            return

        installed = getObject(IInstalledContent(self.context))
        installed.contents += (name,)
        notify(ObjectModifiedEvent(installed))

        self.request.response.redirect(self.request.URL)
