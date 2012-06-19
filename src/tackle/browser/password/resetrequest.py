# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.component import getUtility
from tackle.interfaces import IPasswordResetUtility

class Pagelet:

    done = False

    def update(self):
        login = self.request.get('login')

        if login:
            pwdreset = getUtility(IPasswordResetUtility)
            try:
                pwdreset.request(login, self.request)
            except KeyError:
                pass
            self.done = True
