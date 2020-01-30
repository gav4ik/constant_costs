from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class Page():

    def __init__(self, driver):
        self.driver = driver
        self.datetime_from_id = "date-from"
        self.datetime_to_id = "date-to"
        self.chosen_service = "Survey"
        self.choose_all = "add-service-button"
        self.service = "service"
        self.select_all = "select-all"
        self.name_additional_param = "additional-param-name"
        # self.param = "msisdn"
        self.enter_param_button = "add-param-button"
        self.fulfil_element = "//*[@id='additional-params']/li/input"
        self.show_button = "show-button"


    def enter_data_from(self, data_from):
       self.driver.find_element_by_id(self.datetime_from_id).send_keys(data_from)

    def enter_data_to(self, data_to):
       self.driver.find_element_by_id(self.datetime_to_id).send_keys(data_to)

    def choose_service(self, chosen_service):

        drp = Select(self.driver.find_element_by_id(self.service))
        drp.select_by_visible_text(chosen_service)
        self.driver.find_element_by_id(self.choose_all).click()

    def click_select_all(self):
        self.driver.find_element_by_class_name(self.select_all).click()

    def enter_additional_param(self, param):
        self.driver.find_element_by_id(self.name_additional_param).send_keys(param)

    def click_additional_param(self):
        self.driver.find_element_by_id(self.enter_param_button).click()

    def fulfil_param(self, t):
        self.driver.find_element_by_xpath(self.fulfil_element).send_keys(t)

    def show_click(self):
        self.driver.find_element_by_id(self.show_button).click()










