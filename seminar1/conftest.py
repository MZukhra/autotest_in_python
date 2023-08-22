import pytest
import requests

import yaml

with open("config2.yaml") as f:
    info = yaml.safe_load(f)

username = info['username']
password = info['password']


@pytest.fixture()
def get_token():
    """Авторизация и получение токена"""
    res = requests.post(url=info["url1"], data={"username": username, "password": password})
    token = res.json()["token"]
    return token

@pytest.fixture()
def get_description(get_token):
    """Создание нового поста и получение описания"""
    res = requests.post(url=info["url2"], headers={"X-Auth-Token": get_token}, data={"username": username, "password": password, "title": info["title"],
                                                  "description": info["description"], "content": info["content"]})
    return res.json()["description"]



