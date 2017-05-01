from com.cloudops.genericlib.SolventSelenium import SolventSelenium
import logging
import com.cloudops.genericlib.custom_logger as cl
import time

class RechargePage(SolventSelenium):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locator
    _enter_recharge_amount = "//input[@id='payment_amount' and @type = 'text']"
    _available_balance = "//div[@class= 'box-recharge-sum']//span[text()='Available Balance']//..//h2"
    _radio_payment_100 = "//input[@id = 'payment_amount_100']//..//label[contains(text(),'100')]"
    _radio_payment_500 = "//input[@id = 'payment_amount_500']//..//label[contains(text(),'500')]"
    _radio_payment_1000 = "//input[@id = 'payment_amount_1000']//..//label[contains(text(),'1,000')]"
    _radio_payment_2000 = "//input[@id = 'payment_amount_2000']//..//label[contains(text(),'2,000')]"
    _radio_payment_2500 = "//input[@id = 'payment_amount_2500']//..//label[contains(text(),'2,500')]"
    _promo_code_link = "//a[@href='/coupons/new?service_type=prepaid' and text() = 'Got a promo code?']"
    _recharge_now_button = "//button[text()='Recharge Now']"
    _promo_code_popup = "//div[@class='modal-dialog']//div[text()='Enter your promo code']"
    _enter_promo_code = "//div[@class='modal-dialog']//form[@action = '/coupons/apply']//input[@id='promotional_code']"
    _apply_promo_code = "//div[@class='modal-dialog']//form[@action = '/coupons/apply']//button[text()='Apply']"
    _cancel_promo_code = "//div[@class='modal-dialog']//form[@action = '/coupons/apply']//a[text()='Cancel']"
    _error_message = "//div[@class='modal-dialog']//div[@id='coupon_error']/span"
    _close_promocode_popup = "//div[@class='modal-dialog']//a/img[@alt = 'Close modal']"
    _close_success_promocode_popup = "//div[@id='coupounModal']//a/img[@alt='Close modal']"
    _promocode_success_title = "//div[@id='coupounModal']//div[@class='title' and text()='Promo code success']"
    _billing_info_page = "//h2[text()='Billing Information']"

    def apply_coupon(self, coupon_code):
        self.waitForElement(self._promo_code_link)
        self.elementClick(self._promo_code_link)
        self.waitForElement(self._promo_code_popup)
        self.sendKeys(coupon_code, self._enter_promo_code)
        self.elementClick(self._apply_promo_code)
        time.sleep(5)

    def verify_coupon_success_message(self):
        self.waitForElement(self._promocode_success_title)
        promo_code_success_message = self.getText("//div[@class='imgt-box']")
        expected_message = "Your promo code of ₹ 100 has been applied successfully. Your new credit balance is ₹ "
        if expected_message in promo_code_success_message:
            self.log.info("Actual message : " + promo_code_success_message + "contains the expected message : " + expected_message)
            return True
        else:
            self.log.info(
                "Actual message : " + promo_code_success_message + "does not contain the expected message : " + expected_message)
            return False

    def verify_used_coupon_message(self):
        used_coupon_message = self.getText("//div[@id='coupon_error']//span")
        expected_error_message = "Sorry. This promo code has been used"
        if used_coupon_message == expected_error_message:
            self.log.info("Actual message : " + used_coupon_message + "is same as the expected message : " + expected_error_message)
            return True
        else:
            self.log.info("Actual message : " + used_coupon_message + "is not same as the expected message : " + expected_error_message)
            return False

    def verify_incorrect_coupon_message(self):
        incorrect_coupon_message = self.getText("//div[@class='modal-dialog']//div[@id='coupon_error']//span")
        expected_error_message = "Sorry. This promo code is incorrect"
        if incorrect_coupon_message == expected_error_message:
            self.log.info("Actual message : " + incorrect_coupon_message + "is same as the expected message : " + expected_error_message)
            return True
        else:
            self.log.info("Actual message : " + incorrect_coupon_message + "is not same as the expected message : " + expected_error_message)
            return False

    def close_success_promocode_popup(self):
        self.waitForElement(self._close_success_promocode_popup)
        self.elementClick(self._close_success_promocode_popup)
        time.sleep(3)
        self.waitForElement(self._recharge_now_button)

    def get_available_balance_on_recharge_page(self):
        balance = self.getText(self._available_balance)
        return balance[2:-2]

    def verify_available_balance(self, expected_balance):
        self.page_reload()
        current_balance = self.get_available_balance_on_recharge_page()
        if expected_balance == float(current_balance.replace(',', '')):
            self.log.info("Current Balance : " + str(current_balance) + "is same as the expected balance : " + str(expected_balance))
            return True
        else:
             self.log.info("Current Balance : " + str(current_balance) + "is not same as the expected balance : " + str(expected_balance))
             return False

    def click_on_available_recharge_options(self, amount):
        time.sleep(2)
        self.elementClick("//input[@id = 'payment_amount_" + amount.replace(',', '') + "']//..//label[contains(text(),'" + amount + "')]")

    def verify_amount_in_amount_textfield(self, amount):
        actual_amount = self.getText(self._enter_recharge_amount)
        if amount == actual_amount:
            self.log.info("Expected amount : " + amount + " is same as the actual amount present in the amount text field : " + actual_amount)
            return True
        else:
            self.log.info(
                "Expected amount : " + amount + " is not same as the actual amount present in the amount text field : " + actual_amount)
            return False

    def enter_amount(self, amount):
        time.sleep(3)
        self.sendKeys(amount, self._enter_recharge_amount)

    def click_on_recharge_now(self):
        self.elementClick(self._recharge_now_button)
        self.waitForElement(self._billing_info_page)





