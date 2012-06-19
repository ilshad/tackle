from zope.interface import Interface
from zope.schema import TextLine, Int, Text, List

class IFirstExampleConfig(Interface):

    param1 = TextLine(
        title=u'Param1',
        default=u'foo')

    param2 = List(
        title=u'Param2',
        value_type=TextLine(),
        default=[u'bar', u'baaz'])

class ISecondExampleConfig(Interface):

    param1 = Text(
        title=u'Param1',
        default=u'foo')

    param2 = Int(
        title=u'Param2',
        default=10)
