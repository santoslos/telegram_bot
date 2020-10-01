import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = 'https://ru.dotabuff.com/heroes/abaddon'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
driver.get("https://ru.dotabuff.com/heroes/abaddon")
elem = driver.find_element_by_xpath("//div[@class = 'col-8']/section[5]").find_elements_by_tag_name('tr')
elem_text = []

i = 0
a = ''
elem.pop(0)
for elemens in elem:
    elem_cell = []
    for j in elemens.find_elements_by_tag_name('td'):
        elem_cell.append(j.text)
    del elem_cell[0]
    elem_text.append(elem_cell)
driver.close()
print(elem_text)
