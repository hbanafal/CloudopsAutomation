from com.cloudops.pagelib.LoginPage import LoginPage
import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest

@pytest.mark.usefixtures("launch_browser")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_login_with_invalid_cred(self):
        self.lp.login_with_invalid_credentials("hemant.singh@sd2labs.com", "password2")
        result = self.lp.verify_invalid_error_message()
        self.ts.markFinal("test_login_with_invalid_cred", result, "Login with invalid credentials verified")

    @pytest.mark.run(order=1)
    def test_login_without_password(self):
        self.lp.login_with_invalid_credentials("hemant.singh@sd2labs.com")
        result = self.lp.verify_invalid_error_message()
        self.ts.markFinal("test_login_without_password", result, "Login without password verified")

    @pytest.mark.run(order=3)
    def test_login(self):
        self.lp.login("hemant.singh@sd2labs.com", "password")
        result = self.lp.verify_login_successful("Hemant Uncle")
        self.ts.markFinal("test_login", result, "Login withvalid credentials verified")

    @pytest.mark.run(order=4)
    def test_logout(self):
        self.lp.logout_user()
        result = self.lp.verify_user_logout()
        self.ts.markFinal("test_logout", result, "Logout is verified")



