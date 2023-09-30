import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = 'https://eproc.setadiran.ir/eproc/entry.do'
driver.get(url)
# wait = WebDriverWait(driver, 10)
# driver.implicitly_wait(20)
time.sleep(5)

xpath = '//*@id="aList"/tbody'
elem = driver.find_element(By.XPATH, xpath)

print('elem is: ' , elem.text)
# for e in elem:
#     print(e.text)
#     print('*'*20)
# driver.close()


# r = requests.get(url).content

# # print(r)

# soup = BeautifulSoup(r, 'html.parser')

# rows = soup.find_all('tbody')

# print(rows)
# # print(soup.prettify())



