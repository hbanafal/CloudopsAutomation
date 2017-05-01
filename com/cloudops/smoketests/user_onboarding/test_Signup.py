import pytest
import unittest
from com.cloudops.pagelib.SignupPage import SignupPage
from com.cloudops.genericlib.TestStatus import TestStatus
from random import choice
from string import ascii_lowercase


@pytest.mark.usefixtures("launch_browser")
class SignupTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, launch_browser):
        self.signup = SignupPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_signup(self):
        email_id = (''.join(choice(ascii_lowercase) for i in range(12))) + "@gmail.com"
        self.signup.signup("Hemant Singh", email_id, "9090909090", "password", "USD")

        result = self.signup.verify_email_confirmation_page()
        self.ts.markFinal("test_signup", result, "Sign up verified")

    @pytest.mark.run(order=1)
    def test_signup_with_existing_email(self):
        self.signup.signup("Hemant Singh", "hemant.singh@sd2labs.com", "9090909090", "password", "INR")

        result = self.signup.verify_existing_user_error()
        self.ts.markFinal("test_signup_with_existing_email", result, "Signup with existing email is verified")