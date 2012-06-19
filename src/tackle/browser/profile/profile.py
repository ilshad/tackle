# 2010 Ilshad Khabibullin <astoon@spacta.com>

from z3c.formui import form
from z3c.form import field

from zope.component import getUtility

from tackle.interfaces import IPrincipalProfileType

""" Edit user profile.
"""

class Pagelet(form.EditForm):

    def __init__(self, context, request):
        iface = getUtility(IPrincipalProfileType, request.get('type') or 'basic')
        self.fields = field.Fields(iface)
        super(Pagelet, self).__init__(context, request)
