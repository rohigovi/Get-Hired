import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Job import Job

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)


def get_url(position = "data scientist", location = "Pittsburgh, PA"):
    template = 'https://www.ziprecruiter.com/candidate/search?search={}&location={}'
    url = template.format(position, location)
    driver.get(url)
    time.sleep(1)


def get_records(job_article):
    try:
        company_name = job_article.find_element(By.CLASS_NAME, "t_org_link").text
    except AttributeError:
        company_name = ''
    try:
        job_location = job_article.find_element(By.CLASS_NAME, "location").text
    except AttributeError:
        job_location = ''
    try:
        job_title = job_article.find_element(By.CLASS_NAME, "just_job_title").text
    except AttributeError:
        job_title = ''
    try:
        job_summary = job_article.find_element(By.CLASS_NAME, "job_snippet").text
    except AttributeError:
        job_summary = ''
    return company_name, job_location, job_title, job_summary


def search_dir():
    job_list = []
    el = driver.find_element(By.ID, "createAlertPop")
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(el, 5, 5)
    action.click()
    action.perform()
    jobs_articles = driver.find_elements(By.CLASS_NAME, "job_content")
    for job_article in jobs_articles:
        record = get_records(job_article)
        job = Job(record[0], record[1], record[2], record[3])
        job_list.append(job)
    for job in job_list:
        print(job.__str__())


if __name__ == '__main__':
    get_url()
    search_dir()
