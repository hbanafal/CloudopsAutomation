from com.cloudops.genericlib.SolventSelenium import SolventSelenium


class FullAccountHistory(SolventSelenium):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _full_account_history_title = "//h2[text()='Account Details']"
    _backtodashboard_link = "//a[@href='/prepaid/dashboard' and text() = 'Back to Upfront Cloud Wallet dashboard']"
    _view_all_previous_recharge_link = "//a[@href='/prepaid/payment_history' and text() = '(View all)']"

    def verify_full_account_history_page_title(self):
        return self.isElementPresent(self._full_account_history_title)

    def click_on_backtodashboard_link(self):
        self.elementClick(self._backtodashboard_link)

    def click_on_viewall_recharges_link(self):
        self.elementClick(self._view_all_previous_recharge_link)
