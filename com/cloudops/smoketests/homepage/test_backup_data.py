from com.cloudops.pagelib.LoginPage import LoginPage
import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.HomePage import HomePage

@pytest.mark.usefixtures("launch_browser", "login")
class backup_data(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_backup_data(self):
        home = HomePage(self.driver)
        home.click_start_need_developer()
        result = home.verify_thankyou_popup()
        self.ts.markFinal("test_backup_data", result, "Thank you pop up on Backup Data card verified")




