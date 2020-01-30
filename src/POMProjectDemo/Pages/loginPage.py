from src.POMProjectDemo.Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        # self.username_textbox_id = "txtUsername" //когда импортировали класс Locators, то:
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"
        self.invalidUsername_message_id = "spanMessage"


    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear # стерли предыдущее
        # self.driver.find_element_by_id(self.username_textbox_id).send_keys(username) # заменили "txtUsername" на self.username_textbox_id и "Admin" на username
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear # стерли предыдущее
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password) # заменили "txtPassword" на self.password_textbox_id и "admin123" на password

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def check_invalid_username_message(self):
        msg = self.driver.find_element_by_id(self.invalidUsername_message_id).text
        return msg