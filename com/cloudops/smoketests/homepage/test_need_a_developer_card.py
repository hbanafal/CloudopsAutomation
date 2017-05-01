from com.cloudops.pagelib.LoginPage import LoginPage
import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.HomePage import HomePage

@pytest.mark.usefixtures("launch_browser", "login")
class need_a_developer(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_need_a_developer(self):
        home = HomePage(self.driver)
        home.click_start_need_developer()
        result = home.verify_redirection("http://beta.engineer.ai/?name=Hemant%20Uncle&email=hemant.singh@sd2labs.com&phone_number=+919096993662/#/need-a-developer")
        self.ts.markFinal("test_need_a_developer", result, "Redirection on Need a developer card verified")




