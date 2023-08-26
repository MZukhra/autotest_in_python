import yaml
from module import Site
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_step1():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == "401", "Test_1 FAIL"

# Задание
# Условие: Добавить в наш тестовый проект шаг добавления поста после входа.
# Должна выполняться проверка на наличие названия поста на странице сразу после его создания.
# Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста.
def test_step2():

    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys("user987")
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys("292963b966")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    btn2_selector = '//*[@id="create-btn"]'
    btn2 = site.find_element("xpath", btn2_selector)
    btn2.click()
    x_selector3 = """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
    input3 = site.find_element("xpath", x_selector3)
    input3.send_keys("user9875")
    x_selector4 = """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
    input4 = site.find_element("xpath", x_selector4)
    input4.send_keys("new user")
    x_selector5 = """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""
    input5 = site.find_element("xpath", x_selector5)
    input5.send_keys("__^_^__")
    time.sleep(testdata["sleep_time"])
    btn3_selector = """//*[@id="create-item"]/div/div/div[7]/div/button/span"""
    btn3 = site.find_element("xpath", btn3_selector)
    btn3.click()
    time.sleep(testdata["sleep_time"])
    x_selector6 = """//*[@id="app"]/main/div/div[1]/h1"""
    title = site.find_element("xpath", x_selector6)
    assert title.text == "user9875", "Test_2 FAIL"



