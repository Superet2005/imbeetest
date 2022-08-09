from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    StaleElementReferenceException, ElementClickInterceptedException


class Common:

    def __init__(self, driver, maxWaitTime):
        self.driver = driver
        self.maxWaitTime = maxWaitTime
        self.retryTime = 0.5
        self.retryRange = 3

    def click(self, selector, selectorType=None):
        """
        selector: can pass CSS selector or Xpath selector
        selectorType: specify using CSS selector or Xpath. If not specify, selector startswith "/" will use Xpath
        """

        if (selectorType == None) and (selector.startswith("/") == True):
            type = 'xpath'
        elif (selectorType == None) and (selector.startswith("/") == False):
            type = 'css'

        for n in range(self.retryRange):
            try:
                if type == "css":
                    WebDriverWait(self.driver, self.maxWaitTime).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))).click()
                    break
                elif type == "xpath":
                    WebDriverWait(self.driver, self.maxWaitTime).until(
                        EC.element_to_be_clickable((By.XPATH, selector))).click()
                    break

            except ElementNotInteractableException:
                time.sleep(self.retryTime)
                print('ElementNotInteractableException retry:', n, selector)
            except StaleElementReferenceException:
                time.sleep(self.retryTime)
                print('StaleElementReferenceException retry:', n, selector)
            except ElementClickInterceptedException:
                time.sleep(self.retryTime)
                print('ElementClickInterceptedException retry:', n, selector)

    def visibility(self, selector, selectorType=None):

        if (selectorType == None) and (selector.startswith("/") == True):
            type = 'xpath'
        elif (selectorType == None) and (selector.startswith("/") == False):
            type = 'css'

        if type == "css":
            WebDriverWait(self.driver, self.maxWaitTime + 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        elif type == "xpath":
            WebDriverWait(self.driver, self.maxWaitTime + 10).until(
                EC.visibility_of_element_located((By.XPATH, selector)))

    def elementsList(self, selector, selectorType=None):

        if (selectorType == None) and (selector.startswith("/") == True):
            type = 'xpath'
        elif (selectorType == None) and (selector.startswith("/") == False):
            type = 'css'

        try:
            if type == "css":
                list = self.driver.find_elements_by_css_selector(selector)
            elif type == "xpath":
                list = self.driver.find_elements_by_xpath(selector)
        except NoSuchElementException:
            return None

        return list

    def elementsAttribute(self, selector, cssProperty, selectorType=None):

        if selectorType == "webElement":
            type = 'webElement'
        elif (selectorType == None) and (selector.startswith("/") == True):
            type = 'xpath'
        elif (selectorType == None) and (selector.startswith("/") == False):
            type = 'css'

        if type == "css":
            result = WebDriverWait(self.driver, self.maxWaitTime).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))).value_of_css_property(cssProperty)
        elif type == "xpath":
            result = WebDriverWait(self.driver, self.maxWaitTime).until(
                EC.element_to_be_clickable((By.XPATH, selector))).value_of_css_property(cssProperty)
        elif type == "webElement":
            result = selector.value_of_css_property(cssProperty)

        return result

    def sendKey(self, key, selector, selectorType=None):

        if (selectorType == None) and (selector.startswith("/") == True):
            type = 'xpath'
        elif (selectorType == None) and (selector.startswith("/") == False):
            type = 'css'

        if type == "css":
            WebDriverWait(self.driver, self.maxWaitTime).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))).send_keys(key)
        elif type == "xpath":
            WebDriverWait(self.driver, self.maxWaitTime).until(
                EC.presence_of_element_located((By.XPATH, selector))).send_keys(key)

    def executeScript(self, script):
        self.driver.execute_script(script)

    def waitForRequest(self, endpoint):
        self.driver.wait_for_request(endpoint)

    def clearReuests(self):
        del self.driver.requests