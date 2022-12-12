#Our Test
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from Training_Page import TrainingGroundPage
from Trail_Page import TrailPage
from Base_Element import BaseElement

#Test Setup
browser = webdriver.Chrome()
test_value = "Hola"

#Trial Page
trial_Page = TrailPage(driver=browser)
trial_Page.go()
trial_Page.stone_input().input_text("rock")
trial_Page.stone_button.click()
input()

#Training Grounds
training_Page = TrainingGroundPage(driver=browser)
training_Page.go()
assert training_Page.button1().text() == 'Button1', "Unexpected button1 text"
input ()
browser.quit()
