# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.event import notify
from zope.component import getUtility
from zope.pluggableauth import PluggableAuthentication
from zope.authentication.interfaces import IAuthentication
from zope.app.authentication import principalfolder, groupfolder
from zope.securitypolicy.interfaces import IPrincipalRoleManager
from zope.principalannotation.interfaces import IPrincipalAnnotationUtility
from zope.principalannotation.utility import PrincipalAnnotationUtility
from zope.dublincore.interfaces import IZopeDublinCore
from zope.index.text.interfaces import ISearchableText
from zope.catalog.interfaces import ICatalog
from zope.catalog.catalog import Catalog
from zope.catalog.text import TextIndex
from zope.intid import IntIds, IIntIds

from tackle.event import NewLocalSite
from tackle.pwdreset import PasswordResetUtility
from tackle.interfaces import IPasswordResetUtility

def setup_local(e):
    sm = e.manager
    site = sm.__parent__ # root folder

    intids = IntIds()
    sm[u'intids'] = intids
    sm.registerUtility(intids, IIntIds)

    catalog = Catalog()
    sm[u'catalog'] = catalog
    sm.registerUtility(catalog, ICatalog)

    catalog[u'fulltext'] = TextIndex(interface=ISearchableText,
                                     field_name='getSearchableText',
                                     field_callable=True)

    auth = PluggableAuthentication()
    sm[u'authentication'] = auth
    sm.registerUtility(auth, IAuthentication)

    pfolder = principalfolder.PrincipalFolder(prefix='principal.')
    auth[u'principalfolder'] = pfolder
 
    gfolder = groupfolder.GroupFolder(prefix='group.')
    auth[u'groupfolder'] = gfolder

    auth.credentialsPlugins += (u'Session Credentials',)
    auth.authenticatorPlugins += (u'principalfolder', u'groupfolder')

    pran = PrincipalAnnotationUtility()
    sm[u'principalannotation'] = pran
    sm.registerUtility(pran, IPrincipalAnnotationUtility)

    pwdreset = PasswordResetUtility()
    sm[u'passwordreset'] = pwdreset
    sm.registerUtility(pwdreset, IPasswordResetUtility)

    # default bootstrap admin
    login = u"manager"
    password = "password"
    pfolder[login] = principalfolder.InternalPrincipal(login, password, login, u"", "SSHA")
    principal_id = pfolder.prefix + login

    prinrole = IPrincipalRoleManager(site)
    prinrole.assignRoleToPrincipal('tackle.SystemManager', principal_id)

    # all authenticated users are guests by default
    prinrole.assignRoleToPrincipal('tackle.Guest', 'zope.Authenticated')

    # site title
    dc = IZopeDublinCore(site)
    dc.title = u"Tackle"

    # custom local setup
    notify(NewLocalSite(sm))
