import pytest
import requests

import yaml

with open("config2.yaml") as f:
    adress = yaml.safe_load(f)

username = adress['username']
password = adress['password']


@pytest.fixture()
def get_token():
    """Авторизация и получение токена"""
    res = requests.post(url=adress["url1"], data={"username": username, "password": password})
    token = res.json()["token"]
    return token

@pytest.fixture()
def get_description(get_token):
    """Создание нового поста и получение описания"""
    res = requests.post(url=adress["url2"], headers={"X-Auth-Token": get_token}, data={"username": username, "password": password, "title": adress["title"],
                                                  "description": adress["description"], "content": adress["content"]})
    return res.json()["description"]



