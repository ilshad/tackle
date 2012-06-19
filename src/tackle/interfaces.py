# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.interface import interfaces, Interface, Attribute
from zope.schema import List, Choice, TextLine, Password, ASCIILine

class IPrincipalProfileType(interfaces.IInterface):
    """If an interface provides this interface type, then
    we assume that interface defines schema of personal data."""

class IBasicProfile(Interface):
    """Basic user properties,
    principal profile type"""

    name = TextLine(
        title=u'Title',
        required=False)

    email = TextLine(
        title=u'Email',
        required=False)

class IPersistentConfigType(interfaces.IInterface):
    """If an interface provides this interface type, then
    that interface considered as system parameters schema
    interface.

    Configuration system defined by IPersistentConfigType
    and IPersistentConfig and it allows to store
    miscellaneous parameters using authomatically created
    persistent objects contained in special annotation to
    site.

    Let us create arbitrary config.

    Step 1: describe config schema:

    class IMyConfig(Interface):
        param1 = TextLine(title=u"Param 1")
        param2 = Int(title=u"Param 2")

    Step 2: register this interface as IConfigType interface
    type:

    <interface
        interface=".interfaces.IMyConfig"
        type="tackle.interfaces.IPersistentConfigType"
        name="My Config"
        />

    That's it. Now "Me Config" menu item appears in
    system menu (sidebar on context site/++etc++site)
    and corresponding form availabe.

    Usage:

    my_config = tackle.persistent_config("My Config")
    param1 = my_confg.param1
    """

class IPersistentConfig(Interface):
    """Configurable site"""

    def get_config(key):
        """Return custom config bunch with given key"""

class IContentTraverseDefault(Interface):
    """Persistent config: wich content should be
    traversed by default."""

    traverse_default = Choice(
        title=u"Default content to show on frontpage",
        vocabulary="Installed Content",
        required=False,
        default=None)

class IInstalledContent(Interface):
    """Ordered sequence of installed content"""

    contents = List(
        value_type=Choice(vocabulary="Installed Content"),
        default=[],
        required=False)

class IContent(Interface):
    """This is tackle-specific content and it must be
    installed into site."""

class IAddContent(Interface):
    """Install content object"""

    factory = Choice(
        title=u"Content type",
        vocabulary="Content Factories")

    name = ASCIILine(
        title=u"Identifier")

    title = TextLine(
        title=u"Dublin Core Title",
        default=u'',
        required=False)

class ISearchResultItem(Interface):
    """Generalized search result item"""

    title = Attribute("Title")
    description = Attribute("Description")

class ISecuritySettings(Interface):
    """Local security settings"""

    context = Attribute("Project")
    principal_id = Attribute("Principal id")

    roles = List(
        title=u"Roles",
        value_type=Choice(vocabulary="Tackle Roles"),
        default=[],
        required=False)

class IGroupParticipationPrincipal(Interface):
    """Principal participates in groups"""

    groups = List(
        title=u'Groups',
        value_type=Choice(vocabulary="Groups"),
        default=[],
        required=False)

class INewLocalSite(Interface):
    """Event: new Tackle instance created"""

    manager = Attribute("Local site manager")

class ISubscription(Interface):
    """Subcribe and track"""

    def subscribe(principal_id):
        """Subscribe user"""

    def unsubscribe(principal_id):
        """Unsubscribe user"""

    def send(message, subject):
        """Send mail"""

class ISubscribable(Interface):
    """Subscribable content"""

class ISubscriptionEvent(Interface):
    """Event: send mail subscriptions in the context"""

    context = Attribute("Context")
    message = Attribute("Subscrption message")

class IPasswordResetUtility(Interface):
    """Manage password reset using unique keys"""

    def request(login, req):
        """Set unique reset key, send to user.
        `req` argument is browser request.
        """

    def reset(login, code, password):
        """Change password"""

class IPasswordResetRequest(Interface):
    """Event: new password reset request"""

    principal_id = Attribute("Principal ID")

    login = Attribute("Login")

    code = Attribute("Secret code")

    req = Attribute("Browser request")

class IPasswordResetEvent(Interface):
    """Event: password reset done"""

    principal_id = Attribute("Principal ID")

    password = Attribute("New password")
