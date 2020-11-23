from selenium import webdriver
import time
import datetime
import unittest
from login import Login
from envi_setup import EnvironmentSetup


class LoginTest(EnvironmentSetup):

    # Method to test the login flow
    def test_login(self):

        valid_email = "abc"
        valid_password = "xyz"
        env = "https://www.facebook.com/"

        driver = self.driver
        driver.get(env)

        log = login(driver)
        time.sleep(2)

        # Sending the username and password
        log.userName.send_keys(valid_email)
        log.password.send_keys(valid_password)
        log.login.click()