# 2010 Ilshad Khabibullin, <astoon@spacta.com>

import os
import shutil

get_template = lambda name: os.path.join(os.path.dirname(__file__), name)

def create_env(path):
    shutil.copytree(get_template('base_env'), path)
