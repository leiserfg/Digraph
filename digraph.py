# -*- coding: utf-8 -*-

import sublime
import sublime_plugin


class DigraphCommand(sublime_plugin.TextCommand):

    def run(self, edit, character):
        for sel in self.view.sel():
            p = max(sel.a, sel.b)

            r = sublime.Region(p, p - 1)
            _, c = self.view.rowcol(r.a)
            if c == 0:
                self.view.insert(edit, sel.a, character)
                continue
            firstchar = self.view.substr(r.b)
            # ñ  ñ  ñ
            self.view.replace(edit, r, self.digraph(firstchar,
                                                    character))

    def digraph(self, a, b):
        settings = sublime.load_settings("Digraph.sublime-settings")
        digraph_dict = settings.get('digraph_dict', {})
        return digraph_dict.get("%s%s" % (a, b), b)
