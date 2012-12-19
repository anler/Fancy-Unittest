import unittest

from .runner import ColoredTextTestRunner


def main(**kwargs):
    kwargs['testRunner'] = ColoredTextTestRunner
    unittest.main(**kwargs)
