# 2010 Ilshad Khabibullin <astoon@spacta.com>

""" Update password.
"""

from tackle.util import internal_principal

class Pagelet:

    status = u""

    def update(self):
        old = self.request.get('old') 
        new = self.request.get('new')

        if old and new:
            ip = internal_principal(self.request.principal.id)

            if ip.checkPassword(old):
                ip.setPassword(new, "SSHA")
                self.status = u"Password successfully updated"
            else:
                self.status = u"Wrong old password"
