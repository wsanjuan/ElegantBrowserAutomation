from selenium.webdriver.common.by import By
from Base_Element import BaseElement


class TrainingGroundPage(BasePage):
    url = 'https://techstepacademy.com/training-ground/'

    def button1(self):
        return BaseElement(
            driver=self.driver,
            locator=(By.ID,'b1'))
            
