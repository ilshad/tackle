# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.component import getUtility
from zope.authentication.interfaces import IAuthentication
from zope.authentication.interfaces import IAuthenticatedGroup
from zope.authentication.interfaces import IUnauthenticatedGroup
from zope.traversing.browser import absoluteURL

class Pagelet:

    def update(self):
        if self.request.get("back"):
            self.request.response.redirect(
                u"%s/security" % absoluteURL(self.context, self.request))
        else:
            context_url = self.request["context"]
            auth = getUtility(IAuthentication)

            make_url = lambda name:u"%s/++security++%s" % (context_url, name)

            groupfolder = auth[u'groupfolder']
            self.values = []

            for k,v in groupfolder.items():
                self.values.append(
                    {'url':make_url(groupfolder.prefix + k),
                     'title':v.title})

            gr = getUtility(IUnauthenticatedGroup)
            self.values.append(
                {'url':make_url(gr.id),
                 'title':gr.title})

            gr = getUtility(IAuthenticatedGroup)
            self.values.append(
                {'url':make_url(gr.id),
                 'title':gr.title})
