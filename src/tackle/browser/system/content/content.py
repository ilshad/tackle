# 2010 Ilshad Khabibullin, <astoon@spacta.com>

from z3c.formui import form
from zope.component.hooks import getSite

from tackle.browser.system.content import installed, add

class Pagelet(form.Form):

    def update(self):
        site = getSite()

        self.add = add.AddContent(site, self.request)
        self.add.update()

        self.installed = installed.InstalledContent(site, self.request)
        self.installed.update()

        super(Pagelet, self).update()
