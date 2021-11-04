from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class VDIH_connection:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def deleteObject(self):
        self.driver.quit()


span[normalize-space() = 'Deshabilitar aprovisionamiento']
button[normalize-space()= 'Aceptar']
