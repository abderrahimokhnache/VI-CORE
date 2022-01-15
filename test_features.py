from cgitb import reset
import unittest
import Sandbox.search_system as searchsys

class TestFeatures(unittest.TestCase):
    def test_searchsys(self):
        exe = lambda x:searchsys.execute(x)
        self.assertEqual(exe('search') , None)
        
