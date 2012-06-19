# 2010 Ilshad Khabibullin, <astoon@spacta.com>

from z3c.table import table, column
from z3c.pagelet.browser import BrowserPagelet
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.catalog.interfaces import ICatalog
from zope.component import getUtility
from zope.security import checkPermission
from tackle.interfaces import ISearchResultItem

class Pagelet(BrowserPagelet, table.Table):

    __init__ = table.Table.__init__
    _result = []

    def update(self):
        query = self.request.get('form.widgets.searchtext')
        if query:
            catalog = getUtility(ICatalog)
            r = list(catalog.searchResults(fulltext=query))
            self._result = [x for x in r if checkPermission("zope.View", x)]

        table.Table.update(self)

    @property
    def values(self):
        return self._result

class SearchResultLinkColumn(column.Column):

    def renderCell(self, item):
        sri = ISearchResultItem(item)
        return u'<a href="%s">%s</a><br /><em>%s</em>' % (
            absoluteURL(item, self.request), sri.title, sri.description)
