# 2010 Ilshad Khabibullin <astoon@spacta.com>

import re

from zope.component import getUtility
from zope.authentication.interfaces import IAuthentication
from zope.authentication.interfaces import PrincipalLookupError
from zope.app.authentication.groupfolder import GroupInformation

from tackle.interfaces import IBasicProfile

_isdotted = re.compile(
    r"([a-zA-Z][a-zA-z0-9_]*)"
    r"([.][a-zA-Z][a-zA-z0-9_]*)*"
    # use the whole line
    r"$").match

class Pagelet:

    status = None

    def update(self):
        auth = getUtility(IAuthentication)
        groupfolder = auth[u'groupfolder']

        if self.request.get('form.add.submit'):
            name = self.request.get('name')
            title = self.request.get('title')
            description = self.request.get('description', u'')

            if not _isdotted(name):
                self.status = u'Invalid name'
            elif name and title:
                gi = GroupInformation(title, description)
                groupfolder[name] = gi
            else:
                self.status = u'Provide name and title'

        self.groups = []
        for group in groupfolder.values():
            item = {'value': group, 'principals':[]}
            for pid in group.principals:
                try:
                    item['principals'].append(
                        {'title':IBasicProfile(auth.getPrincipal(pid)).name,
                         'id':pid})
                except PrincipalLookupError:
                    pass
            self.groups.append(item)
