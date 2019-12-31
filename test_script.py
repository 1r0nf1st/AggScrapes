"""
A simple selenium test example
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(
            options=chrome_options, executable_path="C:\\Projects\\PersonalGit\\AggScrapes\\chromedriver.exe")
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
            

        except NoSuchElementException as ex:
            self.fail(ex.msg)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
