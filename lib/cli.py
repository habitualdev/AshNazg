import os
import readline
import re

COMMANDS = ['find','load','exit','wipe']
RE_SPACE = re.compile('.*\s+$', re.M)


class Completer(object):

    def _listdir(self, root):
        res = []
        for name in os.listdir(root):
            path = os.path.join(root, name)
            if os.path.isdir(path):
                name = name + os.sep
            res.append(name)
        return res

    def _complete_path(self, path=None):
        if not path:
            return self._listdir('.')
        dirname, rest = os.path.split(path)
        tmp = dirname if dirname else '.'
        res = [os.path.join(dirname, p) for p in self._listdir(tmp) if p.startswith(rest)]
        if len(res) > 1 or not os.path.exists(path):
            return res
        if os.path.isdir(path):
            return [os.path.join(path, p) for p in self._listdir(path)]
        return [path + ' ']

    def complete_load(self, args):
        if not args:
            return self._complete_path('.')
        return self._complete_path(args[-1])

    def complete_exit(self):
        return ["No more options"]

    def complete_wipe(self):
        return ["No undoing this..."]

    def complete(self, text, state):
        buffer = readline.get_line_buffer()
        line = readline.get_line_buffer().split()
        if not line:
            return [c + ' ' for c in COMMANDS][state]
        if RE_SPACE.match(buffer):
            line.append('')
        cmd = line[0].strip()
        if cmd in COMMANDS:
            impl = getattr(self, 'complete_%s' % cmd)
            args = line[1:]
            if args:
                return (impl(args) + [None])[state]
            return [cmd + ' '][state]
        results = [c + ' ' for c in COMMANDS if c.startswith(cmd)] + [None]
        return results[state]



