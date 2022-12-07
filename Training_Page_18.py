from selenium.webdriver.common.by import By
from Base_Element_18 import BaseElement


class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground/'

    def go(self):
        self.driver.get(self.url)

    def button1(self):
        return BaseElement(
            driver=self.driver,
            locator=(By.ID,'b1'))
