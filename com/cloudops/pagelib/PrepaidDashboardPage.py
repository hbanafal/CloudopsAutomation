from com.cloudops.genericlib.SolventSelenium import SolventSelenium

class PrepaidDashboard(SolventSelenium):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _prepaid_dashboard_title = "//div[text()='Wallet']"
    _full_account_history_button = "//a[@href='/prepaid/account_history' and text()='Full Account History']"
    _unbilled_amount_card_title = "//h2[text()='Unbilled Amount']"
    _current_balance_text = "//div[@class='chart-container balance']//span[text()='Current Balance']"
    _last_month_usage_text = "//div[@class='chart-container balance']//span[text()='Last Month Usage']"
    _recent_recharges_text = "//div[@class='table-cont']/span[text()='Recent recharges']"

    def verify_prepaid_dashboard_title(self):
        return self.isElementPresent(self._prepaid_dashboard_title)

    def click_full_account_history_button(self):
        self.elementClick(self._full_account_history_button)

    def verify_unbilled_amount_card_title(self):
        return self.isElementPresent(self._unbilled_amount_card_title)

    def verify_current_balance(self):
        return self.isElementPresent(self._current_balance_text)

    def verify_last_month_usage(self):
        return self.isElementPresent(self._last_month_usage_text)

    def verify_recent_recharges(self):
        return self.isElementPresent(self._recent_recharges_text)



    