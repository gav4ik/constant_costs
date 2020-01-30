from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")

search_field = driver.find_element_by_id("searchInput")
search_field.send_keys("Robotic process automation")

search_button = driver.find_element_by_xpath("//*[@id='search-form']/fieldset/button/i")
search_button.click()

assert "Robotic process automation" in driver.title

driver.quit()

