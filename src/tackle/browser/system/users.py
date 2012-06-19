# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.component import getUtility
from zope.annotation import IAnnotations
from zope.authentication.interfaces import IAuthentication
from zope.app.authentication.principalfolder import InternalPrincipal

from tackle.interfaces import IBasicProfile
from tackle.profile import get_profile

class Pagelet:

    start = 0
    batch_size = 10

    def update(self):
        auth = getUtility(IAuthentication)
        principalfolder = auth[u'principalfolder']

        delete = self.request.get('form.delete.submit')
        reset = self.request.get('form.delete.reset')

        if delete:
            ids = self.request.get('delete')
            if ids:
                for i in ids:
                    del principalfolder[i]

        if self.request.get('form.add.submit'):
            login = self.request.get('user_login')
            name = self.request.get('user_name')
            email = self.request.get('user_email')
            password = self.request.get('user_password')

            if login and name and password and email:
                ip = InternalPrincipal(login, password, login, u'', 'SSHA')
                principalfolder[login] = ip

                profile = get_profile("principal.%s" % login, "basic")
                profile.name = name
                profile.email = email

        if reset or delete:
            self.start = 0
        else:
            self.start = int(self.request.get('start') or self.start)

        search = self.request.get('search')
        names = principalfolder.search({'search': search or ''}, self.start, self.batch_size)

        self.result = []
        for x in names:
            internal_principal = principalfolder[x[len(principalfolder.prefix):]]
            name = IBasicProfile(auth.getPrincipal(x)).name
            self.result.append({'intprin': internal_principal, 'name': name})

        self.total = len(principalfolder)
        self.end = self.start + len(self.result)
        self.more = self.total > self.end and not bool(search)
