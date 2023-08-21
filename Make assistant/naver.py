# 네이버 검색 라이브러리
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_naver(keyword):
    driver = webdriver.Chrome()

    driver.get('https://naver.com')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#query')))
    search_input = driver.find_element(By.CSS_SELECTOR, '#query')
    search_input.send_keys(keyword)
    search_button = driver.find_element(By.CSS_SELECTOR, '#search-btn')
    search_button.click()
    html = driver.page_source
    time.sleep(10)
    driver.quit()

