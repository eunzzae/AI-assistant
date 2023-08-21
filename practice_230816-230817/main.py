from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev")

browser = webdriver.Chrome(options=options)

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

response = browser.get(f"{base_url}{search_term}")

if response.status_code !=200:
    print("Cant request page")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    job_list = soup.find('ul',class_="jobsearch-ResultsList")
    jobs = job_list.find_all('li', recursive=False)
    for job in jobs:
        zone = job.find("div", class_="mosaic-zone")
        if zone == None:
            print("job li")
        else:
            print("mosaic li")
            