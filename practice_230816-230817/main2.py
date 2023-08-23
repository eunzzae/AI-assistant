from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
# bot 인줄 알고 차단당해서 selenium 써야함
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_page_count(keyword):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options = options)
    base_url = "https://kr.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", {"aria-label":"pagination"})
    if pagination == None:
        return 1
    else:
        pages = pagination.find_all("div", recursive = False)
        count = len(pages)
    if count >= 5:
        return 5
    else:
        return count

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("found", pages)
    # page 는 0 부터 시작
    results = []
    for page in range(pages):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Chrome(options = options)

    base_url = "https://kr.indeed.com/jobs"
    final_url = f"{base_url}?q={keyword}&start={page*10}"
    browser.get(final_url)
    print(final_url)

    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_lists = soup.find("ul", class_ = "jobsearch-ResultsList")
    jobs = job_lists.find_all("li", recursive = False)
    # recursive 를 False 로 하면 아랫단계까지 찾는게 아니라 바로 아래 단계에서만 찾는다
    for job in jobs:
        zone = job.find("div", class_ = "mosaic-zone")
    if zone == None: # None 은 없음을 의미, False 랑은 다름
        #anchor = job.select("h2 a") #h2 안에 있는 a 를 가져오기
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_ = "companyName")
        region = job.find("div", class_ = "companyLocation")
        job_data = {
        "link": f"https://kr.indeed.com/{link}",
        "company": company.string,
        "location": region.sting,
        "position": title
        }
        results.append(job_data)
    return results

num = get_page_count("react")
    #result = extract_indeed_jobs("python")
print(num)
print(extract_indeed_jobs("react"))