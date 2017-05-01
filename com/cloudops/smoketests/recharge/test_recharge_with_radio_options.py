from com.cloudops.pagelib.LoginPage import LoginPage
import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.HomePage import HomePage
from com.cloudops.pagelib.BillingInfoPage import BillingInfoPage
from com.cloudops.pagelib.RechargePage import RechargePage

@pytest.mark.usefixtures("launch_browser", "login")
class Recharge_With_RadioOptions(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_recharge_with_radio_buttons(self):
        home = HomePage(self.driver)
        home.recharge_now()
        recharge_page = RechargePage(self.driver)
        recharge_page.click_on_available_recharge_options("2,000")
        recharge_page.click_on_recharge_now()
        billing_info = BillingInfoPage(self.driver)
        billing_info.enter_billing_info("Hemant", "Sodala,Jaipur", "Jaipur", "Rajasthan", "302019")
        result = billing_info.verify_payment_gatewaye_page()
        self.ts.markFinal("test_recharge_with_radio_buttons", result, "Recharge with available recharge radio options is verified")




