#Our Test
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from PageObject_18 import TrainingGroundPage
from Base_Element_18 import BaseElement

#Test Setup
browser = webdriver.Chrome()
test_value = "Hola"

#The Test
training_Page = TrainingGroundPage(browser)
training_Page.go()
assert training_Page.button1().text() == 'Button1'
