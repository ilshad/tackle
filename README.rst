Tackle
======

.. contents::

Overview
--------

Note: this project is not supported anymore. It was experiment with design
models (but used in some production envoironments also).

Tackle is business oriented content management system written
on top of Python and BlueBream.

Tackle software features:

1. Our deployment policy is to build rich and powerful virtual environment
from start, downloading as much as possible Python/ZTK packages and allow
users to develop plugins ("tacklets") with them. We do not speculate about
a minimalism when it comes to software dependencies. All dependencies are
in your virtual environment from start. Use them.

2. Taclke is not CMS for building piblic web sites.

3. We provide 2 packages: `Tackle` and `Tacklets`. First is CMS. It provides
common functionality to build web applications. Customizable user profiles, security
settings, skin and etc. But it does not provide any end-user useful functionality,
related to any content management. In other words, Tackle package provides
empty, bare, very special CMS.

4. Second package contains some useful open source plugins
("tacklets"). The package "Tacklets" is just convenient way to start use
tackle. Thus you do not need Tacklets package to work with Tackle, generally.

Install Tackle: common way
--------------------------

Install Tackle in 3 steps: install system dependencies, create
virtual environment, install python packages.

NOTE: you don't need to download package "Tackle", because `pip`
utility is downloading it from internet.

1. Install system dependencies
++++++++++++++++++++++++++++++

Install required packages. In Ubuntu, it is::

  $ sudo apt-get install python-dev build-essential libxml2-dev libxslt-dev

In Slackware just make sure `D` software series is installed.

2. Create virtual environment
+++++++++++++++++++++++++++++

It is strong recommended to use virtualenv, because we going to downloading
and install number of ZTK packages.

For this, we provide requirements file. This file is allowing you to build
good virtual environment with all the required packages. Create the sandbox
with this virtual environment using `virtualenv <http://virtualenv.openplans.org>`_.
We're assuming, for example, the filesystem path for the environment will
be `~/sandbox`::

  $ virtualenv --no-site-packages --distribute ~/sandbox

3. Install packages
+++++++++++++++++++

Install Tackle software within the sandbox::

  $ wget http://download.spacta.com/tackle/requirements.txt
  $ ~/sandbox/bin/pip install -r requirements.txt

This will download and install all the required packages into the
sandbox, including "Tackle" and "Tacklets" packages.

That's it. Create application instances, see section "Tackle instance".

Install Tackle: development mode
--------------------------------

Follow 1 and 2 steps from previous section (install system dependencies
and create virtual environment). Then get repositories::

  $ git clone git://github.com/ilshad/tackle.git
  $ git clone git://github.com/ilshad/tacklets.git

Download and install all ZTK packages. For this, use requirements file
from "Tackle" package:

  $ ~/sandbox/bin/pip install -r tackle/maintain/requirements.txt

Install "Tackle" and "Tacklets" packages in development mode::

  $ cd tackle
  $ ~/sandbox/bin/pip install -e .

  $ cd ../tacklets
  $ ~/sandbox/bin/pip install -e .

Of course, "Tacklets" package is optional - you do not need it to
run Tackle at all.

Tackle instance
----------------

Create Tackle instance "sample"::

  $ ~/sandbox/bin/tackle create sample

and run server::

  $ ~/sandbox/bin/tackle daemon sample

Get quick help::

  $ ~/sandbox/bin/tackle help

Take a look sample/etc/site.zcml, edit it if necessary, then restart
server.
