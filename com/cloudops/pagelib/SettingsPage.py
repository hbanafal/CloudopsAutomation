from com.cloudops.genericlib.SolventSelenium import SolventSelenium
import time

class Settings(SolventSelenium):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.waitForElement(self._settings_page_title)

    #Locators
    _settings_page_title = "//div[text()='Settings']"
    _name_text_field = "//input[@id='user_name' and @type='text']"
    _company_name_text_field = "//input[@id='user_company_name' and @type='text']"
    _company_url_field = "//input[@id='user_website_link' and @type='text']"
    _current_password_field = "//input[@id='user_current_password' and @type='password']"
    _new_password_field = "//input[@id='user_password' and @type='password']"
    _confirm_new_pwd_field = "//input[@id='user_password_confirmation' and @type='password']"

    def verify_settings_page_title(self):
        return self.isElementPresent(self._settings_page_title)

    def change_name(self, new_name):
        self.click_edit("name")
        self.clear_text_field(self._name_text_field)
        self.sendKeys(new_name, self._name_text_field)
        self.click_save_changes("name")

    def change_company_name_and_url(self, new_company_name, new_url):
        self.click_edit("company")
        self.clear_text_field(self._company_name_text_field)
        self.sendKeys(new_company_name, self._company_name_text_field)
        self.clear_text_field(self._company_url_field)
        self.sendKeys(new_url, self._company_url_field)
        self.click_save_changes("company")

    def change_password(self, old_password, new_password):
        self.click_edit("password")
        time.sleep(1)
        self.sendKeys(old_password, self._current_password_field)
        self.sendKeys(new_password, self._new_password_field)
        self.sendKeys(new_password, self._confirm_new_pwd_field)
        self.click_save_changes("password")
        time.sleep(1)


    def click_edit(self, setting_type):
        self.elementClick("//div[@id='accordion-sett']//div[@id='" + setting_type + "']//a[text()='Edit']")

    def click_save_changes(self, setting_type):
        self.elementClick("//div[@data-header='" + setting_type + "']//button[text()=' Save Changes']")

    def verify_company_name_and_url(self, expected_company_name, expected_url):
        self.click_edit("company")
        actual_company_name = self.get_attribute_value("value", self._company_name_text_field)
        actual_url = self.get_attribute_value("value", self._company_url_field)
        return expected_company_name == actual_company_name and expected_url == actual_url

    def verify_company_url(self, expected_url):
        self.click_edit("company")
        actual_url = self.getText(self._company_url_field)
        return expected_url == actual_url