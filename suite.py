import unittest
from R1Backoffice import TestScripts



# get all tests from SearchText and HomePageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase(TestScripts)
 
# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([search_text])
 
# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)