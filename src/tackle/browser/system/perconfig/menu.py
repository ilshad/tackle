# 2010 Ilshad Khabibullin <astoon@spacta.com>

import cgi

from zope.component import getUtilitiesFor, hooks
from zope.traversing.browser.absoluteurl import absoluteURL

from tackle.interfaces import IPersistentConfigType

class PersistentConfigMenu:

    def update(self):
        active = self.request.getURL().split('/')[-1].split('@@')[-1] == 'config'
        site_url = absoluteURL(hooks.getSite(), self.request)
        self.menu = []
        for name, _ in getUtilitiesFor(IPersistentConfigType):
            self.menu.append(
                u'<a class="action %s" href="%s/++etc++site/config?type=%s">%s</a>' % (
                    active and self.request.get('type') == name and 'active' or '',
                    site_url,
                    cgi.escape(name),
                    name))

    def render(self):
        return u"".join(self.menu)
