import unittest
import search_system as ssys

class Test_Search_Sys(unittest.TestCase):

    def test_search_service(self):
        self.assertEqual(ssys.parse('search for x on google') , ("google","x"))
        self.assertEqual(ssys.execute("search for x in google"),
                        ( 'google search',["Here is what I found for x on google"]))

if __name__ == "__main__" :
    unittest.main()
