from com.cloudops.genericlib.SolventSelenium import SolventSelenium


class MigrationDashboard(SolventSelenium):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _migration_dashboard_title = "//section[@id='migration_dashboard']//div[text()='Migrate']"
    _full_account_history_button = "//a[@href='/prepaid/account_history' and text()='Full Account History']"
    _unbilled_amount_card_title = "//h2[text()='Unbilled Amount']"
    _current_balance_text = "//div[@class='chart-container balance']//span[text()='Current Balance']"
    _last_month_usage_text = "//div[@class='chart-container balance']//span[text()='Last Month Usage']"
    _recent_recharges_text = "//div[@class='table-cont']/span[text()='Recent recharges']"

    def verify_migration_dashboard_title(self):
        return self.isElementPresent(self._migration_dashboard_title)



