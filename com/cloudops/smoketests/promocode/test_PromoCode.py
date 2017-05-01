from com.cloudops.pagelib.LoginPage import LoginPage
import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.HomePage import HomePage
from com.cloudops.pagelib.RechargePage import RechargePage


@pytest.mark.usefixtures("create_inr_coupon", "launch_browser", "login")
class PromoCode(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, create_inr_coupon, launch_browser, login):
        self.ts = TestStatus(self.driver)
        self.recharge_page = RechargePage(self.driver)

    @pytest.mark.run(order=1)
    def test_promo_code(self):
        home = HomePage(self.driver)
        home.recharge_now()
        available_balance = self.recharge_page.get_available_balance_on_recharge_page()
        self.recharge_page.apply_coupon(self.coupon_code)
        result1 = self.recharge_page.verify_coupon_success_message()
        self.ts.mark(result1, "## Valid promo code is verified ## ")
        self.recharge_page.close_success_promocode_popup()
        updated_balance = float(available_balance.replace(',', '')) + 100
        result2 = self.recharge_page.verify_available_balance(updated_balance)
        self.ts.mark(result2, "## Updated balance verified ## ")
        self.recharge_page.apply_coupon(self.coupon_code)
        result = self.recharge_page.verify_used_coupon_message()
        self.ts.markFinal("test_promo_code", result, "## Promo code is verified ## ")
        self.recharge_page.close_success_promocode_popup()

    @pytest.mark.run(order=3)
    def test_incorrect_promo_code(self):
        home = HomePage(self.driver)
        home.recharge_now()
        self.recharge_page.apply_coupon("INCORRECT1234")
        result = self.recharge_page.verify_incorrect_coupon_message()
        self.ts.markFinal("test_incorrect_promo_code", result, "## Incorrect coupon code verified ##")
