import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.SideNavigation import SideNavigationPanel
from com.cloudops.pagelib.SettingsPage import Settings

@pytest.mark.usefixtures("launch_browser", "login")
class NavigationToSettings(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_navigation_to_settings(self):
        side_menu = SideNavigationPanel(self.driver)
        side_menu.open_side_panel()
        side_menu.navigate_to_settings()
        settings = Settings(self.driver)
        result = settings.verify_settings_page_title()
        self.ts.markFinal("test_navigation_to_settings", result, "Navigation to Settings page from Side Menu is verified")




