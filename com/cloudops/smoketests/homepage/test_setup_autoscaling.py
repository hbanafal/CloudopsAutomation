from com.cloudops.pagelib.LoginPage import LoginPage
import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.HomePage import HomePage

@pytest.mark.usefixtures("launch_browser", "login")
class setup_autoscaling(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_setup_autoscaling(self):
        home = HomePage(self.driver)
        home.click_start_need_developer()
        result = home.verify_thankyou_popup()
        self.ts.markFinal("test_setup_autoscaling", result, "Thank you pop up on Setup Autoscaling card verified")




