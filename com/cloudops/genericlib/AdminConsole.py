from selenium import webdriver
from com.cloudops.genericlib.SolventSelenium import SolventSelenium
import logging
import com.cloudops.genericlib.custom_logger as cl
import time


class AdminConsole():

    log = cl.customLogger(logging.INFO)

    def launch_adminconsole(self):
        self.log.info("Launching Firefox browser")
        self.driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        self.driver.implicitly_wait(5)
        # Maximize the window
        self.driver.maximize_window()
        self.log.info("# Loading browser with Admin Console URL")
        self.driver.get("https://staging.cloudops.ai/admin")
        selenium = SolventSelenium(self.driver)
        self.log.info("Login in admin console")
        selenium.sendKeys("admin@example.com", "//input[@id='admin_user_email']")
        selenium.sendKeys("******", "//input[@id='admin_user_password']")
        selenium.elementClick("//input[@type='submit' and @value='Login']")
        selenium.waitForElement("//h2[text()='Dashboard']")
        return selenium


    def create_new_coupon(self, coupon_type):
        selenium = self.launch_adminconsole()
        self.log.info("Navigate to Coupon page")
        selenium.elementClick("//a[text()='AWS Prepaid']")
        selenium.waitForElement("//a[@href='/admin/coupons' and text() = 'Coupons']")
        selenium.elementClick("//a[@href='/admin/coupons' and text() = 'Coupons']")
        time.sleep(3)
        self.log.info("Open New Coupon form")
        selenium.waitForElement("//a[@href='/admin/coupons/new' and text() = 'New Coupon']")
        selenium.elementClick("//a[@href='/admin/coupons/new' and text() = 'New Coupon']")
        self.log.info("Create INR coupon")
        selenium.waitForElement("//input[@type='submit' and @value='Create Coupon']")
        selenium.sendKeys("100", "//input[@id='coupon_amount']")
        time.sleep(1)
        #selenium.elementClick("//form[@id='new_coupon']//select[@id='coupon_currency_id']")
        #time.sleep(1)
        #selenium.elementClick("//select[@id='coupon_currency_id']/option[text()='" + coupon_type + "']")
        selenium.select_by_visible_text(coupon_type, "coupon_currency_id", locatorType="id")
        selenium.sendKeys("1", "//input[@id='coupon_number_of_coupons']")
        selenium.elementClick("//input[@type='submit' and @value='Create Coupon']")
        selenium.waitForElement("//h2[text()='Coupons']")
        coupon_code = selenium.getText("//table[@id='index_table_coupons']//tbody//tr[1]//td[3]")
        self.driver.quit()
        self.log.info("Coupon is successfully created : " + coupon_code)
        return coupon_code



