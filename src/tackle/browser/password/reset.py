# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.component import getUtility
from tackle.interfaces import IPasswordResetUtility

class Pagelet:

    done = False

    def update(self):
        submit = self.request.get('submit')
        code = self.request.get('reset_code')
        login = self.request.get('reset_login')
        password = self.request.get('reset_password')

        if submit and login and code and password:
            pwdreset = getUtility(IPasswordResetUtility)
            pwdreset.reset(login, code, password)
            self.done = True
