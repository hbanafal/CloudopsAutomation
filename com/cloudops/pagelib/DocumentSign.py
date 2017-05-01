from com.cloudops.genericlib.SolventSelenium import SolventSelenium

class DocuSign(SolventSelenium):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.waitForElement("//button[@id='action-bar-btn-continue' and text()='Continue']", locatorType="xpath", timeout=30, pollFrequency=0.5)

    #Locators
    _top_continue_button = "//button[@id='action-bar-btn-continue' and text()='Continue']"
    _start_button = "//button[@id='navigate-btn']/span[text()='Start']"
    _sign_button = "//div[@class='page-tabs']//button//div[text()='Sign']"
    _top_finish_button = "//button[@id='action-bar-btn-finish' and text()='Finish']"
    _progress_indicator = "//div[@id='progress-indicator']//div[@class='spinner']"

    def sign_document(self):
        self.wait_for_element_to_disappear(self._progress_indicator)
        self.waitForElement(self._top_continue_button)
        self.elementClick(self._top_continue_button)
        self.elementClick(self._start_button)
        self.waitForElement(self._sign_button)
        signatures = self.getElements(self._sign_button)
        for sign in signatures:
            sign.click()
        self.elementClick(self._top_finish_button)

    def sign_terms_and_conditions(self):
        self.wait_for_element_to_disappear(self._progress_indicator)
        self.waitForElement(self._top_continue_button)
        self.elementClick(self._top_continue_button)
        self.elementClick(self._start_button)
        self.waitForElement(self._sign_button)
        self.elementClick(self._sign_button)
        self.elementClick(self._top_finish_button)

