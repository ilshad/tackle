# 2010 Ilshad Khabibullin <astoon@spacta.com>

from persistent import Persistent
from zope.component import adapts, hooks
from zope.component.interfaces import ISite
from zope.schema.fieldproperty import FieldProperty
from zope.interface import implements
from zope.annotation import factory

from tackle.interfaces import IInstalledContent

class InstalledContent(Persistent):
    implements(IInstalledContent)
    adapts(ISite)

    contents = FieldProperty(IInstalledContent['contents'])

annotation_factory = factory(InstalledContent)

def content_removed(ob, event):
    annotation = IInstalledContent(getSite())
    keys = annotation.contents
    name = event.oldName
    if name in keys:
        x = keys.pop(keys.index(name))
