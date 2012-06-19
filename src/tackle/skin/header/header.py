# 2010, Ilshad Khabibullin, <astoon@spacta.com>

from zope.component.hooks import getSite
from zope.contentprovider.provider import ContentProviderBase
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.dublincore.interfaces import IZopeDublinCore

class Header(ContentProviderBase):

    def render(self):
        site = getSite()
        return u'<h1><a href="%s">%s</a></h1>' % (
            absoluteURL(site, self.request),
            IZopeDublinCore(site).title)
