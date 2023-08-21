# 네이버 검색 라이브러리
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 네이버 검색 기능 구현
# 크롬 드라이버 파일 경로 

def search_naver(keyword):
    driver = webdriver.Chrome()
    # 네이버 크롬 브라우저에 접근할 것을 지정
    driver.get('https://naver.com')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#query')))
    # 검색창 요소 특정
    search_input = driver.find_element(By.CSS_SELECTOR, '#query')
    # key 값을 지정 변수 search_name
    search_input.send_keys(keyword)
    #검색 버튼 특정
    search_button = driver.find_element(By.CSS_SELECTOR, '#search-btn')
    search_button.click()
    html = driver.page_source
    time.sleep(10)
    driver.quit()
    # soup = BeautifulSoup(html, 'html.parser')
    # a_elements = soup.select('a')
    # print(a_elements)

