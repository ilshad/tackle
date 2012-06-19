# 2010 Ilshad Khabibullin, <astoon@spacta.com>

import urllib

from zope.app.security.interfaces import IUnauthenticatedPrincipal
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.cachedescriptors.property import Lazy
from zope.component.hooks import getSite, getSiteManager

from tackle.interfaces import IBasicProfile

class SimpleMenuItem(object):

    available = True

    def render(self):
        return u'<a href="%s/%s">%s</a>' % (
            absoluteURL(getSite(), self.request),
            self.__name__, self.title)

class ItemAuthenticated(object):

    css_class = u''

    def siteURL(self):
        return absoluteURL(getSite(), self.request)

    @property
    def available(self):
        return not IUnauthenticatedPrincipal(self.request.principal, False)

    def render(self):
        return u'<a href="%s" class="%s">%s</a>' % (
            self.url, self.css_class, self.title)

class ItemUnauthenticated(ItemAuthenticated):

    @property
    def available(self):
        return IUnauthenticatedPrincipal(self.request.principal, False)

class UserName(ItemAuthenticated):

    def render(self):
        return u'''<span class="username">%s</span>
                ''' % IBasicProfile(self.request.principal).name

class Home(object):

    def render(self):
        return u'<a href="%s">Home</a>' % absoluteURL(getSite(), self.request)

class Profile(ItemAuthenticated):

    def render(self):
        return u'<a href="%s/++user++%s?type=basic">Profile</a>' % (
            absoluteURL(getSite(), self.request), self.request.principal.id)

class Login(ItemUnauthenticated):

    def render(self):
        return u'<a href="%s/@@login.html">%s</a>' % (self.siteURL(), self.title)
        #return u'<a href="%s/@@login.html?nextURL=%s">%s</a>' % (
        #    self.siteURL(), urllib.quote(self.request.getURL()), self.title)

class Logout(ItemAuthenticated):

    def render(self):
        return u'<a href="%s/@@logout.html?nextURL=%s">%s</a>' % (
            self.siteURL(), urllib.quote(self.siteURL()), self.title)

class System(object):

    available = True

    def render(self):
        return u'<a href="%s">%s</a>' % (absoluteURL(getSiteManager(), self.request), self.title)

class EmptyItem(object):

    def render(self):
        return u""
