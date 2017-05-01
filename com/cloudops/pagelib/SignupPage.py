from com.cloudops.genericlib.SolventSelenium import SolventSelenium
import logging
import com.cloudops.genericlib.custom_logger as cl

class SignupPage(SolventSelenium):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locator
    _company_field = "//input[@id='user_company_name']"
    _email_field = "//input[@id='user_email']"
    _phone_number_field = "//input[@id='user_phone_number']"
    _password_field = "//input[@id='user_password']"
    _password_confirm_field = "//input[@id='user_password_confirmation']"
    _register_button = "//button[text()='Register']"
    _currency_dropdown = "//select[@id='currency_dropdown']"
    _email_confirm_page_header = "//h2"
    _existing_email_error_message = "//div//input[@id='user_email']/following-sibling::span[@class='error']"

    def select_currency(self, currency):
        self.elementClick(self._currency_dropdown)
        self.waitForElement("//select[@id='currency_dropdown']//option[text()='" + currency + "']")
        self.elementClick("//select[@id='currency_dropdown']//option[text()='" + currency + "']")

    def signup(self, companyName, email, phoneNumber, password, currency):
        self.sendKeys(companyName, self._company_field)
        self.sendKeys(email, self._email_field)
        self.sendKeys(phoneNumber, self._phone_number_field)
        self.sendKeys(password, self._password_field)
        self.sendKeys(password, self._password_confirm_field)
        self.select_currency(currency)
        self.elementClick(self._register_button)
        self.waitForElement("//h2[contains(text(), 'Email Confirmation')]")

    def verify_email_confirmation_page(self):
        headertext = self.getText(self._email_confirm_page_header)
        expectedheader = "Email Confirmation"
        if headertext == expectedheader:
            self.log.info("Actual header : " + headertext + "is matched to expected header text : " + expectedheader)
            return True
        else:
            self.log.info("Actual header : " + headertext + "is not matched to expected header text : " + expectedheader)
            return False

    def verify_existing_user_error(self):
        actual_error = self.getText(self._existing_email_error_message)
        expected_error = "Email has already been taken"
        if actual_error == expected_error:
            self.log.info("Actual error message : " + actual_error + " is matched to expected error message :"
                          + expected_error)
            return True
        else:
            self.log.info("Actual error message : " + actual_error + " is not matched to expected error message :"
                          + expected_error)
            return False
