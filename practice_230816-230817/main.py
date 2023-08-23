from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver

# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome

def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("cant request page")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        pagination = soup.find("ul", class_="pagination-list")
        pages = pagination.find_all("li", recursive=False)
        print(len(pages))
        
def extract_indeed_jobs(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("cant request page")
    else:
        results = []
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find('ul',class_="jobsearch-ResultsList")
        jobs = job_list.find_all('li', recursive=False)
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find('span', class_='companyName')
                location = job.find('dic', class_='companyLocation')
                job_data = {
                    'link':f"https://kr.indeed.com{link}",
                    "company":company.string,
                    "location":location.string,
                    "position":position.string
                }
                results.append[job_data]
        for result in results:
            print(result, "\n/////////////////\n")
            
        while (True):
            pass