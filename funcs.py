from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service



def fetch_data(df):
    '''
    fetch data in current page and save them in an excel file.
    '''

    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)

    # url0 = 'https://eproc.setadiran.ir/eproc/entry.do' 
    # url = 'https://eproc.setadiran.ir/eproc/needs.do'
    url = 'https://eproc.setadiran.ir/eproc/needs.do?pager=true&d-146909-p=1'

    for i in range(1,21):
        url = f'https://eproc.setadiran.ir/eproc/needs.do?pager=true&d-146909-p={i}'
        driver.get(url)

        # Wait until the element is visible
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="aList"]/tbody')))
        # find tr tags
        tr_tags = element.find_elements(By.TAG_NAME, 'tr')    
    
        # a counter to find duplicated items
        duplicated_counter = 0

        for tr_tag in tr_tags:
            td = tr_tag.find_elements(By.TAG_NAME, 'td')
            print('inner loop')

            
            no = td[0].text
            need_number = td[1].text # need_number
            description = td[2].find_element(By.TAG_NAME, 'span').get_attribute('title') # description
            organization = td[3].find_element(By.TAG_NAME, 'span').get_attribute('title') # organization
            province = td[4].find_element(By.TAG_NAME, 'span').get_attribute('title') # province
            need_type = td[5].find_element(By.TAG_NAME, 'span').get_attribute('title') # need_type
            category = td[6].text # category
            goods_group = td[7].find_element(By.TAG_NAME, 'span').get_attribute('title') # goods_group
            service_group = td[8].find_element(By.TAG_NAME, 'span').get_attribute('title') # service_group
            published_date = td[9].find_element(By.TAG_NAME, 'span').text # published_date
            deadline = td[10].find_element(By.TAG_NAME, 'span').get_attribute('title') # deadline

            row = {
                'No.' : no,
                'need_number': need_number,
                'description': description,
                'organization' : organization,
                'province' : province,
                'need_type' : need_type,
                'category' : category,
                'goods_group' : goods_group,
                'service_group' : service_group,
                'published_date' : published_date,
                'deadline' : deadline
            }
            df = df._append(row, ignore_index=True)
            df = df.fillna('')


            if df['need_number'].duplicated().any():
                df = df.drop(df.tail(1).index)
                print('DUPLICATED ROW')
                duplicated_counter += 1
                if duplicated_counter == 3:
                    print('BREAK')
                    return 0
        
        df.to_excel(r"setadiran-scraper\data\test.xlsx")