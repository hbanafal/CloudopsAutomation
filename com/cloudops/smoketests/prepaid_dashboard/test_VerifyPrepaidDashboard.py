from com.cloudops.pagelib.PrepaidDashboardPage import PrepaidDashboard
import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.HomePage import HomePage

@pytest.mark.usefixtures("launch_browser", "login")
class VerifyPrepaidDashboard(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_prepaid_dashboard_content(self):
        home = HomePage(self.driver)
        home.view_prepaid_dashboard()
        dashboard = PrepaidDashboard(self.driver)
        result1 = dashboard.verify_prepaid_dashboard_title()
        self.ts.mark(result1, "Prepaid Dashboard title is verified")
        result2 = dashboard.verify_unbilled_amount_card_title()
        self.ts.mark(result2, "Unbilled amount card title is verified")
        result3 = dashboard.verify_current_balance()
        self.ts.mark(result3, "Current Balance text is verified")
        result4 = dashboard.verify_last_month_usage()
        self.ts.mark(result4, "Last month usage text is verified")
        result5 = dashboard.verify_recent_recharges()
        self.ts.markFinal("test_prepaid_dashboard_content", result5, "Recent Recharges table is verified")




