import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.SideNavigation import SideNavigationPanel

@pytest.mark.usefixtures("launch_browser", "login")
class FacebookRedirection(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_facebook_redirection(self):
        side_menu = SideNavigationPanel(self.driver)
        side_menu.open_side_panel()
        side_menu.navigate_to_facebook()
        result = side_menu.verify_redirection("https://www.facebook.com/squaredsd/?fref=ts")
        self.ts.markFinal("test_facebook_redirection", result, "Redirection to Facebook is verified")




