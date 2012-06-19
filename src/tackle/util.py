# 2010 Ilshad Khabibullin <astoon@spacta.com>

import os
import string
import random
import datetime

from zope.component import getUtility
from zope.authentication.interfaces import IAuthentication

def internal_principal(id):
    auth = getUtility(IAuthentication)
    pf = auth[u'principalfolder']
    k = id[len(pf.prefix):]
    return pf[k]

def random_string(length):
    chars = []
    while length:
        chars.extend(random.sample(string.letters+string.digits, 1))
        length -= 1
    return "".join(chars)

def open_file(name, context):
    return open(os.path.join(os.path.dirname(context), name))
