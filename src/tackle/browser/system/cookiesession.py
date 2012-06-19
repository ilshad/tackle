# 2010 Ilshad Khabibullin <astoon@spacta.com>

from z3c.form import field
from z3c.formui import form
from zope.session.http import ICookieClientIdManager
from zope.session.interfaces import IClientIdManager
from zope.component import getUtility

class Pagelet(form.EditForm):

    fields = field.Fields(ICookieClientIdManager).omit("postOnly")

    def getContent(self):
        return getUtility(IClientIdManager)
