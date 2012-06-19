# This is Public Domain and you can use it
# without a warring about copyrights.

# @author Ilshad Khabibullin

import os
import ConfigParser
import urllib

def mkpath(name):
    return os.path.join(os.path.dirname(__file__), name)

def main():
    config = ConfigParser.ConfigParser()
    config.read(mkpath('maintain.ini'))

    # read from zope.org
    bbversions = {}
    for uri in config.get('DEFAULT', 'import_from').split():
        index = ConfigParser.ConfigParser()
        index.readfp(urllib.urlopen(uri))
        bbversions.update(index.items('versions'))

    # bluebream requirements is just ztk.cfg and zopeapp.cfg
    bbreq = open(mkpath(config.get('DEFAULT', 'bluebream_req')), 'w')
    for n,v in bbversions.items():
        bbreq.write('%s==%s\n' % (n,v))
    bbreq.close()

    # old tackle requirements release
    old = open(mkpath(config.get('DEFAULT', 'old_req')))
    old_versions = {}
    for line in old.readlines():
        item = line.strip() 
        if not item.startswith('#'):
            n,v = item.split('==')
            old_versions[n] = v
    old.close()

    # parse `thirdparty` and `toolkit`
    log = open(config.get('DEFAULT', 'log'), 'w')
    thirdparty = {}
    for n,v in old_versions.items():
        if n in bbversions:
            if v != bbversions[n]:
                log.write('%s : %s -> %s\n' % (n, v, bbversions[n]))
        else:
            thirdparty[n] = v

    # third party packages
    thirdparty_req = open(config.get('DEFAULT', 'thirdparty_req'), 'w')
    for n,v in thirdparty.items():
        thirdparty_req.write('%s==%s\n' % (n,v))
    thirdparty_req.close()

    # truncated bluebream requirements
    tbb_req = open(config.get('DEFAULT', 'truncated_bluebream_req'), 'w')
    log.write('\n\n\n')
    for n,v in bbversions.items():
        if n in old_versions:
            tbb_req.write('%s==%s\n' % (n,v))
        else:
            log.write('%s (%s) from bluebream is not used\n' % (n,v))
    tbb_req.close()
    log.close()

if __name__ == '__main__':
    main()
