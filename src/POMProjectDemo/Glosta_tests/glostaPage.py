class GlostaPage():

    def __init__(self, driver):
        self.driver = driver

        self.data_from = "date-from"
        driver.find_element_by_id("date-from")
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"



#     def enter_password(self, password):
#         self.driver.find_element_by_id(self.password_textbox_id).clear # стерли предыдущее
#         self.driver.find_element_by_id(self.password_textbox_id).send_keys(password) # заменили "txtPassword" на self.password_textbox_id и "admin123" на password
#
#     def click_login(self):
#         self.driver.find_element_by_id(self.login_button_id).click()
#
# search_field1 = driver.find_element_by_id("date-from")
#         search_field1.send_keys("10.12.2019")
#         search_field2 = driver.find_element_by_id("date-to")
#         search_field2.send_keys("11.12.2019")
#         service = driver.find_element_by_id("service")
#         drp = Select(service)
#         drp.select_by_visible_text("Survey")
#         # //*[@id="service"]/option[92]
#         search_button = driver.find_element_by_id("add-service-button")
#         search_button.click()
#         driver.implicitly_wait(5)
#         galka = driver.find_element_by_class_name("select-all")
#         #galka = driver.find_element_by_link_text('Выбрать все')
#         galka.click()
#         driver.implicitly_wait(5)
#         abon = driver.find_element_by_id("additional-param-name")
#         abon.send_keys("msisdn")
#         choose_button = driver.find_element_by_id("add-param-button")
#         choose_button.click()
#         driver.implicitly_wait(5)
#         #tel = driver.find_element_by_class_name("additional-param form-control")
#         tel = driver.find_element_by_xpath("//*[@id='additional-params']/li/input")
#         tel.send_keys("79645860800")
#         driver.implicitly_wait(5)
#         show = driver.find_element_by_id("show-button")
#         show.click()