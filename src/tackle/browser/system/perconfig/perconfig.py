# 2010 Ilshad Khabibullin <astoon@spacta.com>

from z3c.formui import form
from z3c.form import field

from zope.component import getUtility

from tackle.interfaces import IPersistentConfigType
from tackle.perconfig import persistent_config

""" Edit persistent config.
"""

class Pagelet(form.EditForm):

    def __init__(self, context, request):
        self.confname = request.get('type')
        iface = getUtility(IPersistentConfigType, self.confname)
        self.fields = field.Fields(iface)
        super(Pagelet, self).__init__(context, request)

    def getContent(self):
        return persistent_config(self.confname)
