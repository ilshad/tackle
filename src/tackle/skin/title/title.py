# 2010 Ilshad Khabibullin, <astoon@spacta.com>

from zope.component.hooks import getSite
from zope.contentprovider.provider import ContentProviderBase
from zope.dublincore.interfaces import IZopeDublinCore
from zope.security import checkPermission

class BaseTitle(ContentProviderBase):

    def render(self, *args, **kw):
        if checkPermission('zope.View', self.context):
            return IZopeDublinCore(self.context).title
        return u""

class ContentTitle(ContentProviderBase):

    def render(self, *args, **kw):
        site = getSite()
        base = IZopeDublinCore(site).title
        try:
            if checkPermission('zope.View', self.context):
                dc_title = IZopeDublinCore(self.context).title
                if dc_title:
                    return base + u" :: " + dc_title
        except AttributeError: pass
        except TypeError: pass
        return base
