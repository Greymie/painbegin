'''
Created on Nov 13 2014

@author: slukash
'''

#stdlib
import unittest
import time

#selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class LohikasiteReferalCheck(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.wait=WebDriverWait(self.driver, 10)
        self.driver.get("http://www.lohika.com.ua/#vacancies-referral")

    def test_checking_Refs (self):
        referals_1_column = 0
        referals_2_column = 0
        referals_all = 0
        referal_table_slots = self.driver.find_elements_by_xpath(
            './/*[@id="vacancies-referral"]/div[1]/div/div[2]/table/tbody/tr/td')
        for elem in referal_table_slots:
            if elem.text[-1] == '$':
                referals_all = referals_all + int(elem.text[:-1])
                if elem.get_attribute('class') == 'td-1':
                    referals_1_column = referals_1_column + int(elem.text[:-1])
                if elem.get_attribute('class') == 'td-last td-2':
                    referals_2_column = referals_2_column + int(elem.text[:-1])


        print 'all referals', referals_all
        print 'referals from first column', referals_1_column
        print 'refferals from second column', referals_2_column

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()