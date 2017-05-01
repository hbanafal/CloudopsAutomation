from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import com.cloudops.genericlib.custom_logger as cl
import time
import os
from selenium.webdriver.support.select import Select

class SolventSelenium():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../../../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()


    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="xpath"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def getElements(self, locator, locatorType="xpath"):
        elements = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            self.log.info("Elements Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Elements are not found with locator: " + locator + " and  locatorType: " + locatorType)
        return elements

    def elementClick(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="xpath",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def wait_for_element_to_disappear(self, locator, locatorType="xpath",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to disappear")
            wait = WebDriverWait(self.driver, timeout, pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.invisibility_of_element_located((byType, locator)))
            self.log.info("Element disappeared on the web page")
        except:
            self.log.info("Element is still appearing on the web page")
            print_stack()
        return element

    def getText(self, locator, locatorType="xpath"):

        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element found: " + locator)
                return element.text
            else:
                self.log.info("Element not found : " + locator)

        except:
            self.log.info("Element not found : " + locator)

    def page_reload(self):
        self.driver.get(self.driver.current_url)

    def scroll_to_element(self, locator, locatorType="xpath"):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.getElement(locator, locatorType))

    def get_url(self):
        return self.driver.current_url

    def select_by_visible_text(self, option_text, locator, locatorType="xpath"):
        self.log.info("Getting list element")
        select = Select(self.getElement(locator, locatorType))
        try:
            select.select_by_value(2)
            self.log.info("Option is found successfully : " + option_text)
        except:
            self.log.info("Option is not found in the list : " + option_text)

    def verify_redirection(self, expected_url):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        required_url = ""
        timeout = time.time() + 15  # 15 seconds from now
        while True:
            current_url = self.get_url()
            if expected_url in current_url:
                required_url = current_url
                break
            if time.time() > timeout:
                self.log.info("Not redirected to expected url even after 15 seconds. Please check or increase timeout")
                break
        return required_url == expected_url

    def get_attribute_value(self, attribute_name, locator, locatorType="xpath"):
        return self.getElement(locator, locatorType).get_attribute(attribute_name)

    def clear_text_field(self, locator, locatorType="xpath"):
        self.getElement(locator, locatorType).clear()
