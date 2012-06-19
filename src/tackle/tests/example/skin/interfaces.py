from tackle.skin.interfaces import ILayer as base_layer
from z3c.formui.interfaces import IDivFormLayer

class ILayer(base_layer):
    """layer"""

class ISkin(IDivFormLayer, ILayer):
    """skin"""
