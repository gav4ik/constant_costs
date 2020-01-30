from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:/Users/naryshkina/AppData/Local/Microsoft/WindowsApps/chromedriver.exe")

driver.get("https://mfc.ooo-alfatel.ru/statistic/?date_start=2020-01-21&date_end=2020-01-29")
table = driver.find_element_by_xpath("//*[@id='data']/table[1]")
rows = len(driver.find_elements_by_xpath("//*[@id='data']/table[1]/tbody/tr/td"))  # count number of rows
cols = len(driver.find_elements_by_xpath("//*[@id='data']/table[1]/thead/tr"))  # count number of columns

print(rows)
print(cols)


# print("В таблице " + cols + " столбцов.")
# print("В таблице " + rows + " строк.")
# print("В таблице " + cols + " столбцов.")

# all_rows = driver.find_elements_by_xpath("//*[@id='data']/table[1]/tbody/tr/td[1]")

all_rows = driver.find_elements_by_tag_name('tr') # get all the TR elements from the table
# and iterate over them, getting the cells
for row in all_rows:
    cells = row.find_elements_by_tag_name('td')
    dict_value = {'0th': cells[0].text,
                  '1st': cells[1].text,
                  '2nd': cells[2].text,
                  '3rd': cells[3].text,
                  '6th': cells[6].text,
                  '7th': cells[7].text}
    print (cells)
# table.find_elements_by_tag_name("tr")
rows = driver.find_elements_by_tag_name("tr")  # get all of the rows in the table


for row in rows:
        # Get the columns (all the column 2)
    col = row.find_elements_by_xpath("//*[@id='data']/table[1]/tbody/tr/td[1]")  # note: index start from 0, 1 is col 2
    print(col)  # prints text from the element