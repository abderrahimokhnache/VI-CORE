import unittest
import Sandbox.search_system as searchsys
from Core import CEREBRUM

class TestFeatures(unittest.TestCase):
    def test_searchsys(self):
        exe = lambda x:searchsys.execute(x)
        self.assertEqual(exe('search') , None)

    def test_Cerebrum(self):
        exe = lambda x : CEREBRUM.Think(x)
        self.assertTrue(exe('what time is it'))
        self.assertEqual(exe("marvel").tag,"not categorized" )
        self.assertFalse(exe("Hi").tag != "not categorized" )
        self.assertEqual(exe("vi are you up !").output,"for you sir allways")

    def test_nlp(self):
        exe = lambda x : CEREBRUM.Think.NLP(x)
        self.assertEqual(exe("what time is it") , "asking for time")
        self.assertEqual(exe("search for x on x") , "asking to search")
        self.assertEqual(exe("find x.x and open it") , "asking to find a file and open it ")

    