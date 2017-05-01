import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.SideNavigation import SideNavigationPanel
from com.cloudops.pagelib.HomePage import HomePage
from com.cloudops.pagelib.SettingsPage import Settings
from random import choice
from string import ascii_lowercase

@pytest.mark.usefixtures("launch_browser", "login")
class NameSetting(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_change_name(self):
        sidepanel = SideNavigationPanel(self.driver)
        sidepanel.open_side_panel()
        sidepanel.navigate_to_settings()
        settings = Settings(self.driver)
        name = (''.join(choice(ascii_lowercase) for i in range(12)))
        settings.change_name(name)
        sidepanel.open_side_panel()
        sidepanel.navigate_to_home()
        home = HomePage(self.driver)
        result = home.verify_name_on_the_header(name)
        self.ts.markFinal("test_change_name", result, "Name change setting is verified")




