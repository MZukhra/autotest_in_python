from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators():
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_NEW_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")
    LOCATOR_TITLE_TEXT = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_SAVE_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")



class OperationHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_BTN}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD)
        text = error_field.text
        logging.info(f'We find {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def click_to_do_new_post(self):
        logging.info("Click to do new post button")
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_title(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_TITLE_FIELD}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_FIELD)
        title_field.clear()
        title_field.send_keys(word)

    def enter_description(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_DESCRIPTION_FIELD}")
        description_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_FIELD)
        description_field.clear()
        description_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTENT_FIELD}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(word)

    def click_save_button(self):
        logging.info("Click to do new post button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()

    def get_title_text(self):
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_TEXT)
        text = title_field.text
        logging.info(f'We find {text} in error field {TestSearchLocators.LOCATOR_TITLE_TEXT[1]}')
        print(text)
        return text

    def click_contact_button(self):
        logging.info("Click to do new post button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def enter_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD)
        title_field.clear()
        title_field.send_keys(word)

    def enter_email(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD)
        title_field.clear()
        title_field.send_keys(word)

    def enter_contact_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD)
        title_field.clear()
        title_field.send_keys(word)

    def contact_us_save_button(self):
        logging.info("Click to do new post button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_SAVE_BTN).click()



