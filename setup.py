import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(name='Tackle',
      version='0.8.2',
      description='Business oriented CMS',
      long_description = read('README.rst'),
      author='Ilshad Khabibullin',
      author_email='astoon@spacta.com',
      url='',
      test_suite='tackle',
      license="",
      zip_safe=False,
      include_package_data=True,
      packages=find_packages('src'),
      package_dir={'':'src'},
      install_requires=[],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Customer Service',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Framework :: ZODB',
        'Framework :: Zope3'],
      entry_points={'console_scripts': ['tackle = tackle.main:main'],
                    'paste.app_factory': ['main = tackle.serve:app'],
                    'paste.global_paster_command': ['shell = tackle.debug:Shell']}
      )
