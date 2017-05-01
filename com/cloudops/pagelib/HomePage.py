from com.cloudops.genericlib.SolventSelenium import SolventSelenium
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(SolventSelenium):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.waitForElement(
            "//section[@id='cloudops_dashboard']//div[@class='container']//h2[contains(text(),'Upfront Cloud Wallet')]")

    # Start button Locators
    _prepaid_card = "//section[@id='cloudops_dashboard']//div[@class='container']//h2[contains(text(),'Upfront Cloud Wallet')]"
    _start_migration = ""
    _start_prepaid = "//span[@data-target='#serviceDetailPrepaidModal' and text() = 'Start']"
    _start_ubs = "//span[@data-target='#serviceDetailUbsModal' and text() = 'Start']"
    _start_cbs = "//span[@data-target='#serviceDetailCbsModal']"
    _automated_monitoring_start_button = "//a[@href='/accounts/new?service_type=4']/div/span[text()='Start']"
    _backup_data_start_button = "//a[@href='/accounts/new?service_type=4']/div/span[text()='Start']"
    _setup_autoscaling_start_button = "//a[@href='/accounts/new?service_type=4']/div/span[text()='Start']"
    _need_a_developer_start_button = "//a[contains(@href,'need-a-developer')]/div/span[text()='Start']"
    _need_a_devops_start_button = "//a[contains(@href,'need-a-devops')]/div/span[text()='Start']"

    # Other Buttons
    _migrate_another = "//a[@href='/accounts/new' and text() = 'Migrate Another']"
    _recharge_now_button = "//a[@href='/recharge' and text()='Recharge Now']"
    _view_migration_dashboard = "//a[@href='/migration/dashboard' and text()='View Dashboard']"
    _view_prepaid_dashboard = "//a[@href='/prepaid/dashboard' and text()='View Dashboard']"
    _view_migration_account_details = "//div[@class='account_detail']//div[contains(@class,'acc-name') \
             and text() = 'Sdsquared1']//..//a[text()='View details']"
    _recharge_now_page = "//form[@id='new_payment']//div[text()='Recharge']"

    # Modal Box Next button Locator
    _prepaid_modal_next_button = "//div[@id='serviceDetailPrepaidModal']//a[@type='button' and text()='Next']"
    _ubs_modal_next_button = "//div[@id='serviceDetailUbsModal']//a[@type='button' and text()='Next']"
    _cbs_modal_next_button = "//div[@id='serviceDetailCbsModal']//a[@type='button' and text()='Next']"

    # Other Locators
    _thankyou_popup_text = "//div[text()='We have received your request. Our team will get back to you soon.']"
    _name_on_the_header = "//button[@class='dropdown-toggle']//span"

    def start_prepaid(self):
        self.elementClick(self._start_prepaid)
        self.waitForElement(self._prepaid_modal_next_button)
        self.elementClick(self._prepaid_modal_next_button)

    def verify_prepaid_card(self):
        return self.isElementPresent(self._prepaid_card)

    def view_prepaid_dashboard(self):
        self.elementClick(self._view_prepaid_dashboard)

    def start_ubs(self):
        self.elementClick(self._start_ubs)
        self.waitForElement(self._ubs_modal_next_button)
        self.elementClick(self._ubs_modal_next_button)

    def start_cbs(self):
        self.elementClick(self._start_cbs)
        self.waitForElement(self._cbs_modal_next_button)
        self.elementClick(self._cbs_modal_next_button)

    def recharge_now(self):
        self.elementClick(self._recharge_now_button)
        self.waitForElement(self._recharge_now_page)

    def click_start_automated_monitoring(self):
        self.scroll_to_element(self._automated_monitoring_start_button)
        self.elementClick(self._automated_monitoring_start_button)
        self.waitForElement(self._thankyou_popup_text)

    def click_start_backup_data(self):
        self.scroll_to_element(self._backup_data_start_button)
        self.elementClick(self._backup_data_start_button)
        self.waitForElement(self._thankyou_popup_text)

    def click_start_setup_autoscaling(self):
        self.scroll_to_element(self._setup_autoscaling_start_button)
        self.elementClick(self._setup_autoscaling_start_button)
        self.waitForElement(self._thankyou_popup_text)

    def click_start_need_developer(self):
        self.scroll_to_element(self._need_a_developer_start_button)
        self.elementClick(self._need_a_developer_start_button)

    def click_start_need_devops(self):
        self.scroll_to_element(self._need_a_devops_start_button)
        self.elementClick(self._need_a_devops_start_button)

    def verify_thankyou_popup(self):
        return self.isElementPresent(self._thankyou_popup_text)

    def verify_name_on_the_header(self, expected_name):
        actual_name = self.getText(self._name_on_the_header)
        if actual_name == expected_name:
            return True
        else:
            return False

    def get_name_on_the_header(self):
        return self.getText(self._name_on_the_header)
