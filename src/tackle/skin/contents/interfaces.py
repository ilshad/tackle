# 2010 Ilshad Khabibullin, <astoon@spacta.com>

from zope.interface import Interface, Attribute

class IContentMenuItem(Interface):

    css_class = Attribute("CSS class")
    type_title = Attribute("Additional title: content type")

    def render():
        """String representation"""
