import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.SideNavigation import SideNavigationPanel
from com.cloudops.pagelib.PrepaidDashboardPage import PrepaidDashboard

@pytest.mark.usefixtures("launch_browser", "login")
class NavigationToPrepaidDashboard(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_navigation_to_prepaid_dashboard(self):
        sidepanel = SideNavigationPanel(self.driver)
        sidepanel.open_side_panel()
        sidepanel.navigate_to_prepaid_dashboard()
        prepaid_dashboard = PrepaidDashboard(self.driver)
        result1 = prepaid_dashboard.verify_prepaid_dashboard_title()
        self.ts.mark(result1, "Prepaid Dashboard card Title is verified")
        result2 = prepaid_dashboard.verify_unbilled_amount_card_title()
        self.ts.markFinal("test_navigation_to_prepaid_dashboard", result2, "Unbilled amount card title is verified")




