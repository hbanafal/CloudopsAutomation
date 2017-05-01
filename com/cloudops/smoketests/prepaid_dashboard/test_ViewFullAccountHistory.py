from com.cloudops.pagelib.PrepaidDashboardPage import PrepaidDashboard
from com.cloudops.pagelib.FullAccountHistoryPage import FullAccountHistory
from com.cloudops.pagelib.PreviousRechargesPage import PreviousRecharges
import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.HomePage import HomePage

@pytest.mark.usefixtures("launch_browser", "login")
class ViewFullAccountHistory(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_full_account_history(self):
        home = HomePage(self.driver)
        home.view_prepaid_dashboard()
        dashboard = PrepaidDashboard(self.driver)
        dashboard.click_full_account_history_button()
        full_account_history = FullAccountHistory(self.driver)
        result1 = full_account_history.verify_full_account_history_page_title()
        self.ts.mark(result1, "Full Account History Page Title is verified")
        full_account_history.click_on_viewall_recharges_link()
        previous_recharges = PreviousRecharges(self.driver)
        result2 = previous_recharges.verify_previous_recharges_page_title()
        self.ts.mark(result2, "Previous Recharged Page title is verified")
        previous_recharges.click_back_to_account_history_link()
        result3 = full_account_history.verify_full_account_history_page_title()
        self.ts.mark(result3, "Back to Full Account History link from Recharges page is verified")
        full_account_history.click_on_backtodashboard_link()
        result4 = dashboard.verify_prepaid_dashboard_title()
        self.ts.markFinal("test_full_account_history", result4, "Back to Prepaid Dashboard link from Full Account History page is verified")






