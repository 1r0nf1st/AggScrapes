"""
A simple selenium test example
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pyodbc
import time
import datetime
import csv
import sys


class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(
            options=chrome_options)

        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_1(self):
        """Find and click get homeinsurance quote"""
        try:
            self.driver.get('https://www.comparethemarket.com/')
            el = self.driver.find_element_by_id(
                'Market_HomePage_HomepageHeroBlock_HomeInsurance')
            el.click()
            print('Click on quote button done move to write to db')
            time.sleep(30)
            print(pyodbc.drivers())
            self.readCSV()
            self.writeData('data')

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def readCSV(self):
        ifile = open('/code/FixedCTM_segments_Claims.csv')
        reader = csv.reader(ifile)

        for row in reader:
            print(row)
        ifile.close()

    def writeData(self, data):
        print(pyodbc.drivers())
        # print(datetime.datetime.now())
        # time.sleep(240)
        # print('finished sleep for 240')
        # print(datetime.datetime.now())

        conn = pyodbc.connect(
            "DRIVER={SQL Server};SERVER=srv-sql-08;UID=MysteryShopping;PWD=S9htyamncKrjVXHN;DATABASE=MysteryShopping")

        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM MysteryShopping.dbo.MysteryShopping_Test')

        cursor.execute('''
                INSERT INTO MysteryShopping.dbo.MysteryShopping_Test (Agreement_ID,
                Test_Case,
                Date_Captured,
                Aggregator,
                Segment,
                Periodicity,
                Competitor,
                Price,
                RankInQuote,
                Email,
                Customer_Id,
                Focus,
                Segment_Name_for_DW)      
                VALUES
                (1,
                55,
                getdate(),
                'Aggregator',
                'Segment',
                'Periodicity',
                'Competitor',
                55.55,
                100,
                'j@j.com',
                1,
                'Focus',
                'Segment_Name_for_DW')
                ''')
        conn.commit()

        # print('writeData')
        # print(data)
        # print('sleep for 240')
        # print(datetime.datetime.now())
        # time.sleep(240)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
