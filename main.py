
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

# url0 = 'https://eproc.setadiran.ir/eproc/entry.do' 
url = 'https://eproc.setadiran.ir/eproc/needs.do'

driver.get(url)

xpath = '//*[@id="aList"]/tbody'

# Wait until the element is visible
element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

elem = element.find_elements(By.TAG_NAME, 'tr')