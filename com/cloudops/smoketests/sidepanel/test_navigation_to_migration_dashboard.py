import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.SideNavigation import SideNavigationPanel
from com.cloudops.pagelib.MigrationDashboardPage import MigrationDashboard

@pytest.mark.usefixtures("launch_browser", "login")
class NavigationToMigrationDashboard(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_navigation_to_migration_dashboard(self):
        sidepanel = SideNavigationPanel(self.driver)
        sidepanel.open_side_panel()
        sidepanel.navigate_to_migration_dashboard()
        prepaid_dashboard = MigrationDashboard(self.driver)
        result = prepaid_dashboard.verify_migration_dashboard_title()
        self.ts.markFinal("test_navigation_to_migration_dashboard", result, "Migration Dashboard card title is verified")




