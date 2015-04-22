__author__ = 'WP8Dev'
import unittest
from UnitTest_Demo import SearchTest
from UnitTest_Demo2 import SearchTest1
import os
import HTMLTestRunner


def main():
    search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
    search_tests2 = unittest.TestLoader().loadTestsFromTestCase(SearchTest1)
    ## Put them in the Array
    smoke_tests = unittest.TestSuite([search_tests, search_tests2])
    ## File
    dir = os.getcwd()
    outfile = open(dir + "\SmokeTestReport.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream = outfile,title = 'Test Report',description = 'Smoke Tests')
    runner.run(smoke_tests)


if __name__ == "__main__":
    main()