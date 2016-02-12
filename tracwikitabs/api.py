# -*- coding: utf-8 -*-

from trac.core import Component, implements
from trac.web.chrome import ITemplateProvider


class TracWikiTabsSystem(Component):

    implements(ITemplateProvider)

    def get_htdocs_dirs(self):
        from pkg_resources import resource_filename
        return [('wikitabs', resource_filename(__name__, 'htdocs'))]

    def get_templates_dirs(self):
        return ()
