from com.cloudops.pagelib.LoginPage import LoginPage
import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.HomePage import HomePage
from com.cloudops.pagelib.RechargePage import RechargePage


@pytest.mark.usefixtures("create_usd_coupon", "launch_browser", "login")
class USD_Code_In_INR_Account(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, create_usd_coupon, launch_browser, login):
        self.ts = TestStatus(self.driver)
        self.recharge_page = RechargePage(self.driver)

    @pytest.mark.run(order=1)
    def test_usd_code_in_inr_account(self):
        home = HomePage(self.driver)
        home.recharge_now()
        self.recharge_page.apply_coupon(self.coupon_code)
        result = self.recharge_page.verify_incorrect_coupon_message()
        self.ts.markFinal("test_usd_code_in_inr_account", result, "## USD coupon code in INR account is verified ##")
