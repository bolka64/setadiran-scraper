from funcs  import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import pandas as pd

# df = pd.DataFrame(columns=['No.', 'need_number', 'description', 'organization', 'province', 'need_type', 'category', 'goods_group', 'service_group', 'published_date' , 'deadline'])

df = pd.read_excel(r"setadiran-scraper\data\test.xlsx", index_col=0)

fetch_data(df)

