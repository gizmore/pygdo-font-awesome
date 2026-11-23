import unittest

from gdo.icon_fa.IconFA import IconFA
from gdo.ui.IconUTF8 import IconUTF8


class ClockIconTest(unittest.TestCase):
    def test_clock_exists_in_both_providers(self):
        self.assertEqual('🕒', IconUTF8.MAP()['clock'])
        self.assertEqual('clock', IconFA.MAP()['clock'])
