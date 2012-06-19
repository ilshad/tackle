# 2010 Ilshad Khabibullin, <astoon@spacta.com>

from zope.security import checkPermission
from zope.component import getMultiAdapter, hooks
from zope.contentprovider.provider import ContentProviderBase
from zope.location import LocationIterator

from tackle.interfaces import IInstalledContent
from interfaces import IContentMenuItem

class Menu(ContentProviderBase):

    result = u''

    def update(self):
        site = hooks.getSite()
        for name in IInstalledContent(site).contents:
            try:
                ob = site[name]
            except KeyError:
                continue
            if checkPermission('zope.View', ob):
                menu_item = getMultiAdapter((ob, self.request), IContentMenuItem)
                selected = ob in LocationIterator(self.context)
                self.result += menu_item.render(selected)

    def render(self, *args, **kw):
        return self.result
