import sublime_plugin
import os


class PyModuleizeMakeModuleCommand(sublime_plugin.TextCommand):
    def run(self, edit, paths):
        init = '__init__.py'
        for path in paths:
            if os.path.isdir(path):
                for root, _dirs, _files in os.walk(path):
                    init_file = os.path.join(root, init)
                    if not os.path.exists(init_file):
                        with file(init_file, 'w'):
                            pass
