# 2010 Ilshad Khabibullin <astoon@spacta.com>

import os
import ConfigParser

from paste.script import command
from zope.app.wsgi import getWSGIApplication

config = ConfigParser.ConfigParser()

def app(global_conf):
    config.read(global_conf['__file__'])
    return getWSGIApplication(global_conf['zope_conf'])

def serve(path_conf, daemon=False):
    commands = command.get_commands()
    cmd = commands['serve'].load()
    runner = cmd('serve')
    path_env = os.path.dirname(path_conf)
    os.chdir(path_env)
    if daemon:
        runner.run(["--daemon", path_conf])
    else:
        runner.run([path_conf])

def kill(path_conf):
    commands = command.get_commands()
    cmd = commands['serve'].load()
    runner = cmd('serve')
    path_env = os.path.dirname(path_conf)
    os.chdir(path_env)
    runner.run(["--stop-daemon"])
