from com.cloudops.genericlib.SolventSelenium import SolventSelenium
import logging
import com.cloudops.genericlib.custom_logger as cl

class LoginPage(SolventSelenium):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username_field = "//input[@id='user_email']"
    _password_field = "//input[@id='user_password']"
    _login_button = "//button[text()='Login']"
    _login_link = "//a[@href='/login']"
    _userid_on_homepage = "//button[@class='dropdown-toggle']//div[@class='label']//span[@class='wel']"
    _error_message = "//div[@id='alert']"


    def enterUsername(self, username):
        self.sendKeys(username, self._username_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def click_on_loginlink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def get_userid_on_homepage(self):
        return self.getElement(self._userid_on_homepage, locatorType="xpath")

    def login(self, username, password):
        if self.isElementPresent(self._login_link, locatorType="xpath"):
            self.elementClick(self._login_link, locatorType="xpath")
            self.waitForElement(self._login_button, locatorType="xpath")

        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()
        self.waitForElement(self._userid_on_homepage, locatorType="xpath")

    def verify_login_successful(self, expectedUserID):
        userid = self.getText(self._userid_on_homepage, locatorType="xpath")
        if userid == expectedUserID:
            self.log.info("Actual User id :" + userid + " is matched to expected user id :" + expectedUserID)
            return True
        else:
            self.log.info("Actual User id :" + userid + " is not matched to expected user id :" + expectedUserID)
            return False


    def login_with_invalid_credentials(self, username="", password=""):
        if self.isElementPresent(self._login_link, locatorType="xpath"):
            self.elementClick(self._login_link, locatorType="xpath")
            self.waitForElement(self._login_button, locatorType="xpath")

        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def  verify_invalid_error_message(self):
        actual_error_msg = self.getText(self._error_message, locatorType="xpath")
        expected_error_msg = "Invalid credentials"
        if actual_error_msg == expected_error_msg:
            self.log.info("Actual Error msg :" + actual_error_msg +
                          " is matched to expected error msg :" + actual_error_msg)
            return True
        else:
            self.log.info("Actual Error msg :" + actual_error_msg +
                          " is not matched to expected error msg :" + actual_error_msg)
            return False

    def logout_user(self):
        try:
            self.elementClick("//div[@id='log-out']//button//div[@class='label']", locatorType="xpath")
            self.elementClick("//div[@id='log-out']//ul/li//button[text()='Logout']", locatorType="xpath")
            self.waitForElement("//div[@id='logoutModal']//a[@href='/logout']", locatorType="xpath")
            self.elementClick("//div[@id='logoutModal']//a[@href='/logout']", locatorType="xpath")
            self.waitForElement("//a[@href='/login']", locatorType="xpath")
        except:
            self.log.info("Element not found")

    def verify_user_logout(self):
        return self.isElementPresent("//a[@href='/login']", locatorType="xpath")








