from selenium.webdriver.common.by import By
from Base_Element import BaseElement
from Base_Page import BasePage

class TrailPage(BasePage):
    url = 'https://techstepacademy.com/trial-of-the-stones/'

    def stone_input(self):
        locator = (By.CSS_SELECTOR, 'input#r1Input')
        return BaseElement(self.driver, locator)

    @property
    def stone_button(self):
        locator = (By.CSS_SELECTOR, 'button#r1Btn')
        return BaseElement(self.driver, locator)

    def secrets_input(self):
        locator = (By.CSS_SELECTOR, 'input#r2Input')
        return BaseElement(self.driver, locator)

    @property
    def secrets_button(self):
        locator = (By.CSS_SELECTOR, 'button#r2Butn')
        return BaseElement(self.driver, locator)

