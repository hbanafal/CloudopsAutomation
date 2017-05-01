from com.cloudops.genericlib.SolventSelenium import SolventSelenium
import time

class BillingInfoPage(SolventSelenium):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _billing_name = "//input[@id='customerData_billing_name']"
    _billing_telephone = "//input[@id='customerData_billing_tel']"
    _billing_email = "//input[@id='customerData_billing_email']"
    _billing_address = "//input[@id='customerData_billing_address']"
    _billing_city = "//input[@id='customerData_billing_city']"
    _billing_state = "//input[@id='customerData_billing_state']"
    _billing_zip = "//input[@id='customerData_billing_zip']"
    _billing_country = "//select[@id='customerData_billing_country']"
    _paynow_button = "//button[text()='Pay Now']"
    _ccvenue_page = "//div[@id='paymentinformation']//ul//li//span[text()='Credit Card']"

    def enter_billing_info(self, billing_name, billing_address, billing_city, billing_state, billing_zip):
        self.sendKeys(billing_name, self._billing_name)
        self.sendKeys(billing_address, self._billing_address)
        self.sendKeys(billing_city, self._billing_city)
        self.sendKeys(billing_state, self._billing_state)
        self.sendKeys(billing_zip, self._billing_zip)
        self.elementClick(self._paynow_button)

    def verify_payment_gatewaye_page(self):
        time.sleep(3)
        current_url = self.driver.current_url
        if current_url == "https://staging.cloudops.ai/transaction/ccavRequestHandler":
            return True
        else:
            return False

