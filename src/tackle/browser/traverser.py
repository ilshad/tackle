# 2010 Ilshad Khabibullin <astoon@spacta.com>

import tackle

from zope.container.traversal import ItemTraverser

class SiteTraverser(ItemTraverser):

    def publishTraverse(self, request, name):
        conf = tackle.persistent_config("Frontpage")
        if name == 'index.html' and conf.traverse_default is not None:
            return self.context.get(conf.traverse_default)
        return super(SiteTraverser, self).publishTraverse(request, name)

    def browserDefault(self, request):
        conf = tackle.persistent_config("Frontpage")
        if conf.traverse_default is not None:
            return self.context.get(conf.traverse_default), ('index.html',)
        return super(SiteTraverser, self).browserDefault(request)
