# 2010 Ilshad Khabibullin, <astoon@spacta.com>

from z3c.form import form, field
from zope.browserpage import ViewPageTemplateFile
from tackle.interfaces import IInstalledContent

class InstalledContent(form.EditForm):

    template = ViewPageTemplateFile("installed.pt")
    fields = field.Fields(IInstalledContent)
