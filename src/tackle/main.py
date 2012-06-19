# 2010 Ilshad Khabibullin <astoon@spacta.com>

import os
import sys
import pkg_resources

from z3c.testsetup import testrunner
from tackle.instance import create_env
from tackle.serve import serve, kill

version = pkg_resources.get_distribution('tackle').version

def print_help():
    print "\n***********************************************************************"
    print "Usage: tackle [option] [argument]"
    print "    Argument INST is path to .ini file within Tackle instance"
    print "    or just path to Tackle instance (default.ini used)\n"
    print "Opions:"
    print "create INST ... create instance"
    print "serve INST ...... run server for given instance in foreground mode"
    print "daemon INST ... run server for given instance in background mode"
    print "stop INST ..... kill daemon (stop server)"
    print "test PACKAGE .. run tests for given package. Argument is package's name"
    print "help .......... show this message\n"
    print "***********************************************************************\n"

def getconf(arg):
    path_conf = os.path.abspath(arg)
    if os.path.isdir(path_conf):
        path_conf = os.path.join(path_conf, 'default.ini')
    return path_conf

def eqopt(option, key):
    if option == key: return True
    if option == "-" + key: return True
    if option == "--" + key: return True
    return False

def main():
    try:
        option, arg = sys.argv[1], sys.argv[2]
    except IndexError:
        print_help()
        sys.exit(1)

    if eqopt(option, "create"):
        path_env = os.path.abspath(arg)
        if os.access(path_env, os.F_OK):
            print >>sys.stderr, '%s exists, please choose another path' % path_env
            sys.exit(1)
        create_env(path_env)

    elif eqopt(option, "serve"):
        serve(getconf(arg))

    elif eqopt(option, "daemon"):
        serve(getconf(arg), daemon=True)

    elif eqopt(option, "stop"):
        kill(getconf(arg))

    elif eqopt(option, "test"):
        pkg_path = __import__(arg).__path__[0]
        defaults = ['--path', os.path.dirname(pkg_path)]
        testrunner.run(defaults)

    else:
        print >>sys.stderr, '\nUse tackle help\n'

if __name__ == '__main__':
    pkg_resources.require('Tackle==%s' % version)
    main()
