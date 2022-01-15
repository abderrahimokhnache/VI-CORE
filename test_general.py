import unittest
import Sandbox.search_system as searchsys
from Core import CEREBRUM

class TestFeatures(unittest.TestCase):
    def test_searchsys(self):
        exe = lambda x:searchsys.execute(x)
        self.assertEqual(exe('search') , None)

    def test_Cerebrum(self):
        exe = CEREBRUM.Think('what time is it')
        self.assertTrue(exe)       

    