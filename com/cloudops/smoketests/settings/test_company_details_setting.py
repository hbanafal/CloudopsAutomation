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
class CompanyDetialsSetting(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_change_company_details(self):
        sidepanel = SideNavigationPanel(self.driver)
        sidepanel.open_side_panel()
        sidepanel.navigate_to_settings()
        settings = Settings(self.driver)
        name = (''.join(choice(ascii_lowercase) for i in range(12)))
        url = "https://" + (''.join(choice(ascii_lowercase) for i in range(12))) + ".com"
        settings.change_company_name_and_url(name, url)
        sidepanel.open_side_panel()
        sidepanel.navigate_to_settings()
        result = settings.verify_company_name_and_url(name, url)
        self.ts.markFinal("test_change_company_details", result, "Company Details change setting is verified")




