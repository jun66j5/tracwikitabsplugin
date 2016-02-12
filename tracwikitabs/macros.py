# -*- coding: utf-8 -*-

from trac.wiki.formatter import WikiProcessor
from trac.wiki.macros import WikiMacroBase
from trac.web.chrome import Chrome, add_script


class TabsMacro(WikiMacroBase):

    def expand_macro(self, formatter, name, content, args=None):
        req = formatter.req
        Chrome(self.env).add_jquery_ui(req)
        add_script(req, 'wikitabs/main.js')
        if args is None:
            args = {}
        class_ = filter(None, args.get('class', '').split())
        class_.append('tracwikitabs')
        args['class'] = ' '.join(class_)
        div = WikiProcessor(formatter, 'div', args)
        return div.process(content)
