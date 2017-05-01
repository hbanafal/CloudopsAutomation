from com.cloudops.genericlib.SolventSelenium import SolventSelenium
import time

class SideNavigationPanel(SolventSelenium):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _open_side_navigation = "//div[@id='menu']//img[@alt = 'Burger menu']"
    _navigate_to_home = "//div[@id='leftnav']//a[@href = '/dashboard']"
    _navigate_to_migration_dashboard = "//div[@id='leftnav']//a[@href = '/migration/dashboard']"
    _navigate_to_prepaid_dashboard = "//div[@id='leftnav']//a[@href = '/prepaid/dashboard']"
    _navigate_to_ubs_dashboard = ""
    _navigate_to_cbs_dashboard = ""
    _navigate_to_settings_page = "//a[@href='/settings' and text() = 'Settings']"
    _facebook_icon = "//img[@alt='Fb white']"
    _linkedin_icon = "//img[@alt='Ld white']"
    _twitter_icon = "//img[@alt='Twit white']"

    def open_side_panel(self):
        self.elementClick(self._open_side_navigation)
        time.sleep(2)

    def navigate_to_home(self):
        self.elementClick(self._navigate_to_home)
        time.sleep(2)

    def navigate_to_facebook(self):
        self.elementClick(self._facebook_icon)

    def navigate_to_twitter(self):
        self.elementClick(self._twitter_icon)

    def navigate_to_linkedin(self):
        self.elementClick(self._linkedin_icon)

    def navigate_to_settings(self):
        self.elementClick(self._navigate_to_settings_page)
        time.sleep(2)

    def navigate_to_prepaid_dashboard(self):
        self.elementClick(self._navigate_to_prepaid_dashboard)

    def navigate_to_migration_dashboard(self):
        self.elementClick(self._navigate_to_migration_dashboard)



