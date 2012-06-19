=======================
Tackle functional tests
=======================

:doctest:
:functional-zcml-layer: ftesting.zcml

Prepare tests::

  >>> from zope.testbrowser.testing import Browser
  >>> from zope.interface.verify import verifyObject

  >>> root = getRootFolder()

  >>> sm = root.getSiteManager()
  >>> list(sm)
  [u'authentication', u'catalog', u'default', u'intids', u'passwordreset', u'principalannotation']

  >>> list(sm['default'])
  [u'CookieClientIdManager', u'PersistentSessionDataContainer', u'RootErrorReportingUtility']

  >>> root_url = 'http://localhost'
  >>> browser = Browser()

Open ZODB root::

  >>> browser.open(root_url)
  >>> browser.headers['status']
  '200 Ok'

  >>> browser.url
  'http://localhost/@@loginForm.html?camefrom=%2F%40%40index.html'

  >>> browser.getLink(text=u'Tackle').url
  'http://localhost'

  >>> for x in (u'manager', u'Home', u'System', u'Search', u'Log out'):
  ...     x in browser.contents
  False
  False
  False
  False
  False

Sign in::

  >>> browser.getControl(name='login').value='manager'
  >>> browser.getControl(name='password').value='password'
  >>> browser.getControl(name='SUBMIT').click()

  >>> browser.url
  'http://localhost/@@index.html'

  >>> for x in (u'manager', u'Home', u'System', u'Search', u'Log out'):
  ...     x in browser.contents
  True
  True
  True
  True
  True

OK, so logged in. check 'Home' links:

  >>> browser.getLink(text=u'Tackle').url
  'http://localhost'

  >>> browser.getLink(text=u'Home').url
  'http://localhost'

Quick look at search page::

  >>> browser.getLink(text=u'Search').click()
  >>> browser.url
  'http://localhost/search'

  >>> browser.getControl(name='form.widgets.searchtext').value='foo'
  >>> browser.getControl(label='Search').click()
  >>> browser.url
  'http://localhost/search'

Sign out and sign in again:) ::

  >>> browser.getLink(text=u'Log out').click()
  >>> browser.url
  'http://localhost/@@loginForm.html?camefrom=%2F%40%40index.html'

  >>> browser.open('http://localhost/++etc++site')
  >>> browser.url
  'http://localhost/@@loginForm.html?camefrom=%2F%2B%2Betc%2B%2Bsite%2F%40%40title'

  >>> browser.open('http://localhost')
  >>> browser.getControl(name='login').value='manager'
  >>> browser.getControl(name='password').value='password'
  >>> browser.getControl(name='SUBMIT').click()

Go to system settings::

  >>> browser.getLink(text=u'System').click()
  >>> browser.url
  'http://localhost/++etc++site'

Sidebar::

  >>> browser.getLink(text=u'Title').attrs
  {'href': 'http://localhost/++etc++site/title', 'class': 'action active'}

  >>> browser.getLink(text=u'Content').attrs
  {'href': 'http://localhost/++etc++site/content', 'class': 'action '}

  >>> browser.getLink(text=u'Users').attrs
  {'href': 'http://localhost/++etc++site/users', 'class': 'action '}

  >>> browser.getLink(text=u'Groups').attrs
  {'href': 'http://localhost/++etc++site/groups', 'class': 'action '}

  >>> browser.getLink(text=u'Security').attrs
  {'href': 'http://localhost/++etc++site/security', 'class': 'action '}

  >>> browser.getLink(text=u'Session Cookies').attrs
  {'href': 'http://localhost/++etc++site/cookie_session', 'class': 'action '}

Edit site title::

  >>> browser.getLink(text=u'Title').click()
  >>> browser.getControl(label='Title').value=u'Spacta Lab'
  >>> browser.getControl(label='Apply').click()
  >>> browser.url
  'http://localhost/++etc++site/title'

  >>> browser.getLink(text='Spacta Lab').url
  'http://localhost'

Add sample content with title::

  >>> browser.getLink(text=u'Content').click()
  >>> browser.getControl(label=u'Content type').value
  ['example.content']

  >>> browser.getControl(name=u'form.widgets.contents.from').options
  []

  >>> browser.getControl(name=u'form.widgets.contents.to').options
  []

  >>> browser.getControl(label=u'Identifier').value=u'foo'
  >>> browser.getControl(label=u'Dublin Core Title').value=u'Foo Content'
  >>> browser.getControl(label=u'Add').click()

  >>> browser.getControl(name=u'form.widgets.contents.from').options
  []

  >>> browser.getControl(name=u'form.widgets.contents.to').options
  ['foo']

  >>> browser.getLink(text=u'Foo Content').attrs
  {'href': 'http://localhost/foo', 'class': ''}

Add sample content without title::

  >>> browser.getControl(label=u'Identifier').value=u'bar'
  >>> browser.getControl(label=u'Add').click()

  >>> browser.getControl(name=u'form.widgets.contents.from').options
  []

  >>> browser.getControl(name=u'form.widgets.contents.to').options
  ['foo', 'bar']

  >>> browser.getLink(text=u'bar').attrs
  {'href': 'http://localhost/bar', 'class': ''}

Users::

  >>> browser.getLink(text=u'Users').click()
  >>> browser.url
  'http://localhost/++etc++site/users'

  >>> browser.getLink(text=u'manager').url
  'http://localhost/++etc++site/authentication/principalfolder/manager/edit'

Add user::

  >>> browser.getControl(name='user_name').value=u'Frodo Baggins'
  >>> browser.getControl(name='user_email').value=u'frodo@spacta.com'
  >>> browser.getControl(name='user_login').value=u'frodo'
  >>> browser.getControl(name=u'user_password').value=u'1'
  >>> browser.getControl(label=u'Add').click()

  >>> browser.url
  'http://localhost/++etc++site/users'

Edit user::

  >>> browser.getLink(text=u'Frodo Baggins').click()
  >>> browser.url
  'http://localhost/++etc++site/authentication/principalfolder/frodo/edit'

#  >>> browser.getControl(label=u'Title').value=u'Mr. Frodo Baggins'
#  >>> browser.getControl(label=u'Apply').click()
#  >>> 'Data successfully updated.' in browser.contents
#  True
#
  >>> browser.getControl(label=u'Back').click()
  >>> browser.url
  'http://localhost/++etc++site/users'

#  >>> browser.getLink(text=u'Mr. Frodo Baggins').url
#  'http://localhost/++etc++site/authentication/principalfolder/frodo/edit'

Groups::

  >>> browser.getLink(text=u'Groups').click()
  >>> browser.url
  'http://localhost/++etc++site/groups'

Add group::

  >>> browser.getControl(name='name').value='hobbits'
  >>> browser.getControl(name='title').value='Hobbits'
  >>> browser.getControl(name='description').value='They are hobbits!'
  >>> browser.getControl(label='Add').click()

  >>> 'Hobbits' in browser.contents
  True

  >>> 'They are hobbits!' in browser.contents
  True

  >>> browser.getLink(text=u'Edit').click()
  >>> browser.url
  'http://localhost/++etc++site/authentication/groupfolder/hobbits/edit'

  >>> browser.getControl(label='Description').value=u'big-eared'
  >>> browser.getControl(label='Apply').click()
  >>> browser.getControl(label='Back').click()

Add group and delete::

  >>> browser.getControl(name='name').value='orcs'
  >>> browser.getControl(name='title').value='Orcs'
  >>> browser.getControl(name='description').value='They are hobbits!'
  >>> browser.getControl(label='Add').click()

  >>> 'Orcs' in browser.contents
  True

  >>> browser.getLink(url=u'http://localhost/++etc++site/authentication/groupfolder/orcs/edit').click()
  >>> browser.getControl(label='Delete').click()

  >>> 'Remove group' in browser.contents
  True

  >>> 'Orcs' in browser.contents
  True

  >>> browser.getControl(label=u'Cancel').click()
  >>> browser.url
  'http://localhost/++etc++site/authentication/groupfolder/orcs/edit'

  >>> browser.getControl(label='Delete').click()
  >>> browser.getControl(label='Delete').click()
  >>> browser.url
  'http://localhost/++etc++site/groups'

  >>> 'Orcs' in browser.contents
  False

Set group participation for user::

  >>> browser.getLink(text=u'Users').click()
  >>> browser.getLink(text=u'Frodo Baggins').click()

  >>> browser.getControl(name=u'form.widgets.groups.from').options
  ['hobbits']

  >>> browser.getControl(name=u'form.widgets.groups.to').options
  []

Simalate edit form action, using GET::

  >>> browser.open('http://localhost/++etc++site/authentication/principalfolder/frodo/edit?form.widgets.title=Mr.+Frodo+Baggins&form.widgets.password=&form.widgets.groups.to=hobbits&form.widgets.groups-empty-marker=&form.widgets.groups%3Alist=hobbits&form.buttons.apply=Apply')

  >>> 'Data successfully updated.' in browser.contents
  True

  >>> browser.getControl(name=u'form.widgets.groups.from').options
  []

  >>> browser.getControl(name=u'form.widgets.groups.to').options
  ['hobbits']

  >>> browser.getControl(label='Back').click()
  >>> browser.url
  'http://localhost/++etc++site/users'

Security settings::

  >>> browser.getLink(text=u'Security').click()

  >>> 'Select context' in browser.contents
  True

  >>> browser.getLink(text=u'SITE').click()

  >>> 'Select group for' in browser.contents
  True

See default settings - all authenticated users have Guest role::

  >>> browser.getLink(text=u'Authenticated Users').click()
  >>> browser.getControl(name='form.widgets.roles.from').options
  ['tackle.SystemManager', 'tackle.Owner', 'tackle.Viewer', 'tackle.ContentManager']

  >>> browser.getControl(name='form.widgets.roles.to').options
  ['tackle.Guest']

  >>> browser.getControl(label='Back').click()

Unauthenticated users have not roles::

  >>> browser.getLink(text=u'Unauthenticated Users').click()
  >>> browser.getControl(name='form.widgets.roles.from').options
  ['tackle.Guest', 'tackle.SystemManager', 'tackle.Owner', 'tackle.Viewer', 'tackle.ContentManager']

  >>> browser.getControl(name='form.widgets.roles.to').options
  []

  >>> browser.getControl(label='Back').click()

Edit security roles for hobbits::

  >>> browser.getLink(text=u'Hobbit').click()
  >>> browser.getControl(name='form.widgets.roles.from').options
  ['tackle.Guest', 'tackle.SystemManager', 'tackle.Owner', 'tackle.Viewer', 'tackle.ContentManager']

  >>> browser.getControl(name='form.widgets.roles.to').options
  []

  >>> browser.open('http://localhost/++security++group.hobbits/edit?form.widgets.roles.to=tackle.SystemManager&form.widgets.roles-empty-marker=&form.widgets.roles%3Alist=tackle.SystemManager&form.buttons.apply=Apply')

  >>> 'Data successfully updated.' in browser.contents
  True

  >>> browser.getControl(name=u'form.widgets.roles.from').options
  ['tackle.Guest', 'tackle.Owner', 'tackle.Viewer', 'tackle.ContentManager']

  >>> browser.getControl(name=u'form.widgets.roles.to').options
  ['tackle.SystemManager']

  >>> browser.getControl(label='Back').click()
