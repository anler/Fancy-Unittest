import unittest
import functools

from .termcolors import colorize


def wrap_in_color(**kwargs):
    return functools.partial(colorize, **kwargs)

success = wrap_in_color(fg='green', opts=('bold',))
error = wrap_in_color(fg='yellow', opts=('bold',))
failure = wrap_in_color(fg='red', opts=('bold',))


class ColoredStreamWrapper(object):
    def __init__(self, stream):
        self.stream = stream

    def __getattr__(self, name):
        return getattr(self.stream, name)

    def write(self, arg=None):
        if arg:
            if 'E' == arg:
                arg = error(arg)
            elif 'F' == arg or 'FAILED' == arg:
                arg = failure(arg)
            elif 'OK' == arg or '.' == arg:
                arg = success(arg)

        return self.stream.write(arg)

    def writeln(self, arg=None):
        if arg is not None:
            if 'ERROR' in arg:
                arg = error(arg)
            elif 'FAIL' in arg:
                arg = failure(arg)

        return self.stream.writeln(arg)


class ColoredTextTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super(ColoredTextTestResult, self).__init__(*args, **kwargs)
        self.stream = ColoredStreamWrapper(self.stream)


class ColoredTextTestRunner(unittest.TextTestRunner):
    resultclass = ColoredTextTestResult

    def __init__(self, *args, **kwargs):
        super(ColoredTextTestRunner, self).__init__(*args, **kwargs)
        self.stream = ColoredStreamWrapper(self.stream)
