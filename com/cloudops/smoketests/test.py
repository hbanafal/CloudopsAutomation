import unittest

from com.cloudops.genericlib.AdminConsole import AdminConsole
from com.cloudops.genericlib.WebdriverFactory import WebDriverFactory
from com.cloudops.pagelib.DocumentSign import DocuSign
from com.cloudops.pagelib.HomePage import HomePage
from com.cloudops.pagelib.LoginPage import LoginPage


class test(unittest.TestCase):


    def getCoupon(self):
        admin_console = AdminConsole()
        coupon_code = admin_console.create_new_coupon("USD")
        return coupon_code

    def testing(self):
        #coupon_code = self.getCoupon()
        wdf = WebDriverFactory("firefox")
        driver = wdf.getWebDriverInstance()
        self.lp = LoginPage(driver)
        self.lp.login("indiaqa23@gmail.com", "password")
        home = HomePage(driver)
        home.start_cbs()
        docu_sign = DocuSign(driver)
        docu_sign.sign_terms_and_conditions()
        #sidepanel = SideNavigationPanel(driver)
        #sidepanel.open_side_panel()
        #sidepanel.navigate_to_prepaid_dashboard()
        #prepaid_dashboard = PrepaidDashboard(driver)
        #result1 = prepaid_dashboard.verify_prepaid_dashboard_title()
        #print("result : " + str(result1))
        #result2 = prepaid_dashboard.verify_unbilled_amount_card_title()
        #result2 = settings.verify_company_url("https://www,google.com")
        #print("result : " + str(result2))
        #home.recharge_now()
        #recharge_page = RechargePage(driver)
        #recharge_page.enter_amount("25000")
        #recharge_page.click_on_recharge_now()
        #billing_info = BillingInfoPage(driver)
        #billing_info.enter_billing_info("Hemant", "Sodala,Jaipur", "Jaipur", "Rajasthan", "302019")
        #result = billing_info.verify_payment_gatewaye_page()
        #print("Result is : " + str(result))
        #available_balance = recharge_page.get_available_balance_on_recharge_page()
        #recharge_page.apply_coupon(coupon_code)
        #self.log.info("Result is : " + recharge_page.verify_coupon_success_message())
        #recharge_page.close_success_promocode_popup()
        #updated_balance = float(available_balance.replace(',', '')) + 100
        #result = recharge_page.verify_available_balance(updated_balance)
        #recharge_page.apply_coupon(coupon_code)
        #self.log.info("Result is : " + recharge_page.verify_used_coupon_message())
        #recharge_page.close_promocode_popup()