import unittest
import HTMLTestRunner
import os
from R1Backoffice import TestScripts



 
# get the directory path to output report file
dirc = os.getcwd()
# get all tests from SearchText and HomePageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase(TestScripts)
# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([search_text])
# open the report file
outfile = open(dirc + "/TestSummary.html", "w")
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Execution Report', description='Testing Module: R1 backoffice')
# run the suite using HTMLTestRunner
runner.run(test_suite)
    
