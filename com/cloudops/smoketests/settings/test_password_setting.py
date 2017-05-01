import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.SideNavigation import SideNavigationPanel
from com.cloudops.pagelib.HomePage import HomePage
from com.cloudops.pagelib.SettingsPage import Settings
from com.cloudops.pagelib.LoginPage import LoginPage

@pytest.mark.usefixtures("launch_browser", "login")
class PasswordSetting(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)
        yield
        sidepanel = SideNavigationPanel(self.driver)
        sidepanel.open_side_panel()
        sidepanel.navigate_to_settings()
        settings = Settings(self.driver)
        settings.change_password("newpassword", "password")

    @pytest.mark.run(order=1)
    def test_change_password(self):
        sidepanel = SideNavigationPanel(self.driver)
        sidepanel.open_side_panel()
        sidepanel.navigate_to_settings()
        settings = Settings(self.driver)
        settings.change_password("password", "newpassword")
        sidepanel.open_side_panel()
        sidepanel.navigate_to_home()
        home = HomePage(self.driver)
        expected_id = home.get_name_on_the_header()
        login = LoginPage(self.driver)
        login.logout_user()
        login.login("hemant.singh@sd2labs.com", "password")
        result1 = login.verify_invalid_error_message()
        self.ts.mark(result1, "Login with old password is verified")
        login.login("hemant.singh@sd2labs.com", "newpassword")
        result2 = login.verify_login_successful(expected_id)
        self.ts.markFinal("test_change_password", result2, "Login with new password is verified")




