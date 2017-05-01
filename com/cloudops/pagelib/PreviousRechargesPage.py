from com.cloudops.genericlib.SolventSelenium import SolventSelenium


class PreviousRecharges(SolventSelenium):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _previous_recharges_title = "//h2[text()='Recharges']"
    _back_to_account_history_link = "//a[@href='/prepaid/account_history' and text() = 'Back to Account History']"

    def verify_previous_recharges_page_title(self):
        return self.isElementPresent(self._previous_recharges_title)

    def click_back_to_account_history_link(self):
        self.elementClick(self._back_to_account_history_link)


