==========================
Maintain requirements file
==========================

requirements.txt  = [bluebream] - [excesive] + [3rd party] + Tackle + Tacklets.

Run maintain.py script::

  $ python maintain.py

Create virtualenv and install packages from truncated bluebream::

  $ virtualenv --no-site-package --distribute ~/sandbox
  $ ~/sandbox/bin/pip install -r build/tbb-re.txt

Then install `Tackle` and `Tacklets` and run tests for them::

  $ ~/sandbox/bin/tackle --test tackle
  $ ~/sandbox/bin/tackle --test tacklets

You'll see errors.

Now install manually each package from `build/thirdparty-re.txt`
file but the newest version (or version which you need). Run tests again.
Sometimes need decrease some packages' versions.

When tests OK, freeze packages::

  $ ~/sandbox/bin/pip freeze > requirements.txt
