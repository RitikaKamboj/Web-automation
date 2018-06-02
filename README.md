
# Test-automation-Python language


# Introduction

This project is an example for Automation testing of a website using python language.
Automation using python language, all we need is a url of a website then selenium script will run and automate report will be generated in html form, that same report will be extracted in excel sheet using beautiful soup, a module of python and after that this excel report containing testcases report (pass or fail) will be delivered to respected developer who worked on that website.


## Concepts Included

* Parallel test runs
* Common web page interaction methods
* HTML testcases report generation
* Extraction of HTML report i.e Excel report generation using beautiful soup
* Excel report mailed to various developers having testcase report PASS or FAIL

## Tools

* Eclipse (IDE- to run the code)
* Selenium Webdriver
* Firebug


## Requirements

In order to utilise this project you need to have the following installed locally:

* Firefox 42.0 or higher (used by default for UI tests, this can be changed in the code)
* Python 2.7 or python 3.5
* Selenium Webdriver
* HTML Test runner file
* test_HTML Test runner file
* Python modules- Beautiful soup, smptlib 


## Working

Step 1) Installation of Python(3.5 or 2.7) , selenium webdriver for python , geckodriver(firefox) or chromedriver(chrome) , For HTML report- HTML testrunner, test_HTML testrunner and varipus python packages and modules.
Step 2) After installation, URL needed for which testcases to be created. 
Step 3) Python - selenium Code to be written in R1 backoffice file. In this file various testcases is to be written or whatever functions are to be performed should be written in this file using xpath , id locators etc.
Step 4) R1 backoffice file, HTML testrunner file and test_HTML testrunner file to be imported in new file i.e. SeleniumPythonTestSuiteWithHTMLReport. HTML report will be generated and pass or fail testcases will be shown in web form and this file naming Testsummary.html will be placed in given path.
Step 5) Suite file is for multiple scripted file, to run parallel test runs.
Step 6) Soap file contains python module beautiful soup, used to extract data from html report int excel file. Thus, Blastresults.xls report will be generated running soap file.
Step 7) Now, Mail.py file is used to mail the Excel file containing testcases pass or fail to respective developers. 
