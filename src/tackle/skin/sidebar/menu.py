# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.traversing.browser.absoluteurl import absoluteURL

class SimpleMenuItem(object):

    available = True
    
    def absolute_url(self):
        return absoluteURL(self.context, self.request)

    def get_param(self):
        return getattr(self, 'param', None)

    def active(self):
        if self.request.getURL().split('/')[-1].split('@@')[-1] == self.url:
            param = self.get_param()
            if param is not None:
                k,v = tuple(param.split('='))
                if self.request.get(k) == v:
                    return u"active"
            else:
                return u"active"
        return u""

    def render(self):
        param = self.get_param()
        if param is not None:
            render_param = u'?' + param
        else:
            render_param = u''
        return u'<a class="action %s" href="%s">%s</a>' % (
            self.active(),
            self.absolute_url() + '/' + self.url + render_param,
            self.title)
