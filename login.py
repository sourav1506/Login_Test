from selenium.webdriver.common.by import By

from WebAutomation.Src.PageObject.Locators import Locator

class Login(object):

    def __init__(self, driver):
        self.driver = driver

        self.userName = driver.find_element(By.XPATH, Locator.email_id)
        self.password = driver.find_element(By.XPATH, Locator.password)
        self.login = driver.find_element(By.XPATH, Locator.login)