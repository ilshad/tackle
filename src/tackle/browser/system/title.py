# 2010 Ilshad Khabibullin <astoon@spacta.com>

from z3c.form import field
from z3c.formui import form
from zope.component import hooks
from zope.dublincore.interfaces import IZopeDublinCore

class Pagelet(form.EditForm):

    fields = field.Fields(IZopeDublinCore).select("title")

    def getContent(self):
        return hooks.getSite()
