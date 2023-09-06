import yaml
import pytest
import requests
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser1 = testdata["browser"]
    username = testdata['username']
    password = testdata['password']


@pytest.fixture(scope="session")
def browser():
    if browser1 == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def get_token():
    """Получение токена"""
    res = requests.post(url=testdata["url1"], data={"username": username, "password": password})
    yield res.json()["token"]



@pytest.fixture(scope="session")
def get_description(get_token):
    """Создание нового поста и получение описания"""
    res = requests.post(url=testdata["url2"], headers={"X-Auth-Token": get_token},
                        data={"username": username, "password": password, "title": testdata["title"],
                              "description": testdata["description"], "content": testdata["content"]})
    yield res.json()["description"]

