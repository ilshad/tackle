# 2010 Ilshad Khabibullin <astoon@spacta.com>

from persistent import Persistent
from BTrees.OOBTree import OOBTree, OOBucket

from zope.component import adapts, hooks, getUtility
from zope.component.interfaces import ISite
from zope.interface.declarations import Provides
from zope.interface import implements
from zope.annotation import factory

from tackle.interfaces import IPersistentConfig
from tackle.interfaces import IPersistentConfigType

class _config(object):

    def __init__(self, data, iface):
        provides = Provides(_config, iface)
        object.__setattr__(self, '__provides__', provides)
        object.__setattr__(self, '_data', data)
        object.__setattr__(self, '_schema', iface)

    def __getattr__(self, key):
        if key in self._schema:
            try:
                return self._data[key]
            except KeyError:
                return self._schema[key].default
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        if key in self._schema:
            bound = self._schema[key].bind(self)
            bound.validate(value)
            self._data[key] = value
        else:
            raise AttributeError
    
class PersistentConfig(Persistent):
    implements(IPersistentConfig)
    adapts(ISite)

    def __init__(self):
        self.data = OOBTree()

    def get_config(self, key):
        try:
            c = self.data[key]
        except KeyError:
            c = self.data[key] = OOBucket()
        return _config(c, getUtility(IPersistentConfigType, key))

annotation_factory = factory(PersistentConfig)

def persistent_config(k):
    return IPersistentConfig(hooks.getSite()).get_config(k)
