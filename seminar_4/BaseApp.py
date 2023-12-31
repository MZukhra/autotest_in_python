import logging
import requests
import yaml

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    name = testdata["username"]
    paswd = testdata["password"]


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

    def find_element(self, locator, time=30):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator} ")
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f'Property {property} not found in element with locator {locator}')
            return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site")
            start_browsing = None
        return start_browsing

    def alert(self):
        try:
            alert_obj = self.driver.switch_to.alert
            return alert_obj.text
        except:
            logging.exception("Exception with alert")
            return None

    def get_token(self):
        """Получение токена"""
        try:
            res = requests.post(url=testdata["url1"], data={"username": name, "password": paswd})
            return res.json()["token"]
        except:
            logging.exception("Exception with token")
            return None
