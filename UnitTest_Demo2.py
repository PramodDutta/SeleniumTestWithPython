__author__ = 'WP8Dev'
import unittest
from selenium import webdriver


class SearchTest1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.driver.get("http://demo.magentocommerce.com")

    def test_1(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("Phones")
        self.search_field.submit()
        self.button = self.driver.find_element_by_xpath(".//*[@id='search_mini_form']/div[1]/button")
        self.button.click()
        self.products = self.driver.find_elements_by_css_selector("h2.product-name")
        self.assertEqual(len(self.products), 3)
        print(len(self.products))
        

    def test_2(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("Pant")
        self.search_field.submit()
        self.button = self.driver.find_element_by_xpath(".//*[@id='search_mini_form']/div[1]/button")
        self.button.click()
        self.products = self.driver.find_elements_by_css_selector("h2.product-name")
        self.assertEqual(len(self.products), 4)
        print(len(self.products))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)


