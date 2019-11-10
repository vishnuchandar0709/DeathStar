import unittest
import json

from lib.ui.home_page import HomePage
from lib.ui.login_page import LoginPage
from lib.utils import create_driver


class TestLoginS13576(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver.get_driver_instance()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_valid_tc123456(self):
        data = json.load(open('./test/regression/login/S13576.json'))
        # Go to Login page
        self.login_page.wait_for_login_page_to_load()
        # Enter valid Username
        self.login_page.get_username_textbox().send_keys(data['TC123456']['username'])
        # Enter Valid password
        self.login_page.get_password_textbox().send_keys(data['TC123456']['password'])
        # Click on Login Button
        self.login_page.get_login_button().click()
        # Wait for Home Page get Title and verify
        self.home_page.wait_for_home_page_to_load()
        actual_title = self.driver.title
        expected_title = data['TC123456']['home_page_title']
        assert actual_title == expected_title
        # Click on Logout
        self.home_page.get_logout_button().click()
        # Wait for Login page get Title and Verify
        self.login_page.wait_for_login_page_to_load()
        actual_title = self.driver.title
        expected_title = data['TC123456']['login_page_title']
        assert actual_title == expected_title