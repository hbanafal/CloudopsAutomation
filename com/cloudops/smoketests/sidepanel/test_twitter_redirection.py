import logging
from com.cloudops.genericlib.TestStatus import TestStatus
import com.cloudops.genericlib.custom_logger as cl
import pytest
import unittest
from com.cloudops.pagelib.SideNavigation import SideNavigationPanel

@pytest.mark.usefixtures("launch_browser", "login")
class TwitterRedirection(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, launch_browser, login):
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_twitter_redirection(self):
        side_menu = SideNavigationPanel(self.driver)
        side_menu.open_side_panel()
        side_menu.navigate_to_twitter()
        result = side_menu.verify_redirection("https://twitter.com/SquaredSD")
        self.ts.markFinal("test_twitter_redirection", result, "Redirection to Twitter is verified")




