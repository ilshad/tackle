# 2010 Ilshad Khabibullin <astoon@spacta.com>

import time

from persistent import Persistent
from BTrees.OOBTree import OOBTree, OOBucket
from Cheetah.Template import Template

from zope.interface import implements
from zope.component import getUtility, hooks
from zope.container.contained import Contained
from zope.authentication.interfaces import IAuthentication
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.dublincore.interfaces import IZopeDublinCore
from zope.event import notify

from tackle.interfaces import IPasswordResetUtility
from tackle.event import PasswordResetRequest
from tackle.event import PasswordResetEvent
from tackle.util import random_string, internal_principal, open_file
from tackle.profile import get_profile
from tackle.smtp import send_mail

class PasswordResetUtility(Persistent, Contained):
    implements(IPasswordResetUtility)

    def __init__(self):
        self.requests = OOBTree()

    def request(self, login, req):
        auth = getUtility(IAuthentication)
        pf = auth[u'principalfolder']
        if login in pf:
            principal_id = pf.prefix + login
            code = random_string(30)
            data = OOBucket({'id':principal_id, 'time':time.time()})
            self.requests[code] = data
            notify(PasswordResetRequest(principal_id, login, code, req))
        else:
            raise KeyError

    def reset(self, login, code, password):
        auth = getUtility(IAuthentication)
        pf = auth[u'principalfolder']
        if login in pf:
            principal_id = pf.prefix + login
            data = self.requests.get(code)
            if data and data['id'] == principal_id:
                ip = internal_principal(principal_id)
                ip.setPassword(password, "SSHA")
                notify(PasswordResetEvent(principal_id, password))

def password_reset_request(event):
    user = get_profile(event.principal_id, "basic")
    f = open_file('mail/password_reset_request.tmpl', __file__)

    site = hooks.getSite()
    site_url = absoluteURL(site, event.req)
    page_link = u'%s/password_reset' % site_url
    full_link = u'%s?login=%s&code=%s' % (page_link, event.login, event.code)
    dc = IZopeDublinCore(site)

    data = {'name': user.name,
            'code': event.code,
            'page_link': page_link,
            'full_link': full_link,
            'site_title': dc.title,
            'site_url': site_url}

    message = Template(file=f, searchList=[data])

    subject = u'Password reset request'
    send_mail(message,
              subject,
              user.email,
              subtype='html',
              from_header=dc.title,
              to_header=user.name)
