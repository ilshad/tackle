# 2010 Ilshad Khabibullin, <astoon@spacta.com>

from z3c.form.interfaces import IFormLayer
from z3c.layer.pagelet import IPageletBrowserLayer
from z3c.formui.interfaces import IDivFormLayer
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class ILayer(IFormLayer, IPageletBrowserLayer, IDefaultBrowserLayer):
    """Layer"""

class ISkin(IDivFormLayer, ILayer):
    """Skin"""

