# 2010 Ilshad Khabibullin <astoon@spacta.com>

""" Select context to setup security.
"""

from zope.component import hooks
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.dublincore.interfaces import IZopeDublinCore

class Pagelet:

    def values(self):
        site = hooks.getSite()

        yield {'title': u"SITE",
               'url': absoluteURL(site, self.request),
               'nesting': 0}

        for x in site.values():
            yield {'title': IZopeDublinCore(x).title or x.__name__,
                   'url': absoluteURL(x, self.request),
                   'nesting': 1}
