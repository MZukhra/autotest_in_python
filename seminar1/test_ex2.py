import requests

# Написать тест с использованием pytest и requests, в котором:
# Адрес сайта, имя пользователя и пароль хранятся в config.yaml
# conftest.py содержит фикстуру авторизации по адресу
# https://test-stand.gb.ru/gateway/login с передачей
# параметров “username" и "password" и возвращающей токен авторизации
# Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов другого пользователя,
# для этого выполняется get запрос по адресу https://test-stand.gb.ru/api/posts c хедером,
# содержащим токен авторизации в параметре "X-Auth-Token".
# Для отображения постов другого пользователя передается "owner": "notMe".
# http://restapi.adequateshop.com/api/authaccount/registration
# http://restapi.adequateshop.com/api/authaccount/login

# Дом. задание: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
# а потом проверяется его наличие на сервере по полю «описание».
# Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts
# с передачей параметров title, description, content.
import yaml

with open("config2.yaml") as f:
    adress = yaml.safe_load(f)


def token_auth(token):
    res = requests.get(url=adress["url2"], headers={"X-Auth-Token": token}, params={"owner": "notMe"})
    content_var = [item["content"] for item in res.json()['data']]
    return content_var


def test_step2(get_token):
    assert 'Люди заводят собак, а кошки людей. Видно, считают их полезными домашними животными. Кошки очень симпатичные и грациозные животные. Поэтому они популярные и любимые домашние питомцы. Именно с любовью к пушистым и лысым, длиннохвостым и вислоухим, черным, белым, полосатым и пятнистым мы подготовили цитаты и статусы про котов. Кошка — крошечный лев, который любит мышей, ненавидит собак и покровительствует человеку. Я изучил многих философов и многих кошек. Мудрость кошек неизмеримо выше.' in token_auth(
        get_token), "test_step2 FAIL"

def test_step3(get_description):
    assert adress["description"] in get_description, "test_step3 FAIL"

