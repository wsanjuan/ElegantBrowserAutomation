from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(
            self.driver, 10).until(EC.visibility_of_element_located(self.locator))
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(
            self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        element.click()
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def attribute(self, attr_name):
        attribute= self.web_element.get_attribute(attr_name)
        return attribute

    #Nos da el texto del elemento que tenemos
    def text(self):
        text = self.web_element.text
        return text