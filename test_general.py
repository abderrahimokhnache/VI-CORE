import unittest ,clipboard 
import Sandbox.search_system as searchsys
from Core import CEREBRUM
from utilities.text_op import free

class TestFeatures(unittest.TestCase):
    exe = lambda x : CEREBRUM.Think(x)

    def test_searchsys(self):
        exe = lambda x:searchsys.execute(x)
        self.assertEqual(exe('search') , None)

    def test_dummy(self):
        self.assertEqual(TestFeatures.exe("hi dummy give me a random png").output,'random png')
        self.assertEqual("random png",clipboard.paste())

    def test_master(self):
        self.assertEqual(TestFeatures.exe('what is my name').output , "your name is rahim")

    def test_Cerebrum(self):
        self.assertTrue(TestFeatures.exe('what time is it'))
        self.assertEqual(TestFeatures.exe("marvel").tag,"not categorized" )
        self.assertFalse(TestFeatures.exe("Hi").tag != "not categorized" )
        self.assertEqual(TestFeatures.exe("vi are you up !").output,"for you sir allways")
    def test_txtop(self):

        self.assertEqual(free("search for xxx on x")[1] ," xxx ")

    def test_nlp(self):
        exe = lambda x : CEREBRUM.Think.NLP(x)
        self.assertEqual(exe("what time is it") , "asking for time")
        self.assertEqual(exe("search for x on x") , "asking to search")
        self.assertEqual(exe("find x.x and open it") , "asking to find a file and open it ")

    