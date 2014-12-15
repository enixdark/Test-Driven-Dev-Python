from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


# browser = webdriver.PhantomJS()
# browser.get("http://localhost:8000")
#
# assert 'Django' in browser.title

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get("http://localhost:8000")
        self.assertNotIn("Django",self.browser.title)
        self.assertIn("To-Do",self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do",header_text)
        # self.fail("finish the test")
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Buy peacock feathers')

        input_box.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)
        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # self.fail("finish")

if __name__ == '__main__':
    unittest.main()