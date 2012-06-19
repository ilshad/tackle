# 2010 Ilshad Khabibullin, <astoon@spacta.com>

from zope.component import adapts
from zope.interface import Interface, implements
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.dublincore.interfaces import IZopeDublinCore
from tackle.skin.interfaces import ILayer
from interfaces import IContentMenuItem

class ContentMenuItem(object):
    implements(IContentMenuItem)
    adapts(Interface, ILayer)

    css_class = u""
    type_title = u""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def render(self, selected=False):
        try:
            dc = IZopeDublinCore(self.context)
            title = dc.title
        except TypeError:
            title = None
        return u'<a href="%s" class="%s%s">%s%s</a>' % (
            absoluteURL(self.context, self.request),
            selected and u"selected " or u"",
            self.css_class,
            self.type_title,
            title or self.context.__name__)
