import unittest
import datetime
from selenium import webdriver


class EnvironmentSetup(unittest.TestCase):

    # setUP contains the browser setup attributes
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="/home/Drivers/chromedriver"
        )
        print("Run Started at :" + str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        print("------------------------------------------------------------------")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # tearDown method just to close all the browser instances and then quit
    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            print("------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
        cls.driver.close()
        cls.driver.quit()