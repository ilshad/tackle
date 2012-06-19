from persistent import Persistent
from zope.location import Location
from zope.interface import implements
from interfaces import IExampleContent

class ExampleContent(Persistent, Location):
    implements(IExampleContent)
