# 2010 Ilshad Khabibullin, astoon@spacta.com

from zope.component.hooks import getSite
from zope.component import getFactoriesFor, getUtilitiesFor, getUtility
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.authentication.interfaces import IAuthentication
from zope.dublincore.interfaces import IZopeDublinCore
from zope.securitypolicy.interfaces import IRole

from tackle.interfaces import IContent

def tackle_roles(context):
    terms = []
    for name, role in getUtilitiesFor(IRole, context):
        if name[:7] == 'tackle.' or name[:9] == 'tacklets.':
            terms.append(SimpleTerm(name, title=role.title))
    return SimpleVocabulary(terms)

def groups_vocabulary(context):
    auth = getUtility(IAuthentication, context=context)
    groupfolder = auth[u'groupfolder']
    terms = []
    for name, ob in groupfolder.items():
        terms.append(SimpleTerm(name, title=ob.title))
    return SimpleVocabulary(terms)

def installed_content(context):
    site = getSite()
    terms = []
    for name, ob in site.items():
        try:
            dc = IZopeDublinCore(ob)
            title = dc.title
        except TypeError:
            title = None
        terms.append(SimpleTerm(name, title=title or name))
    return SimpleVocabulary(terms)

def content_factories(context):
    terms = []
    for name, factory in getFactoriesFor(IContent):
        terms.append(SimpleTerm(name, title=factory.title))
    return SimpleVocabulary(terms)
