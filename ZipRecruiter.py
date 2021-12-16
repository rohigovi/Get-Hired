import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Job import Job

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)


class ZipRecruiter:
    def __init__(self, position="data scientist", location="Pittsburgh, PA"):
        self.__position = position
        self.__location = location
        self.__job_list = []

    def get_job_list(self):
        return self.__job_list

    # ZipRecruiter called on the driver.
    def get_url(self):
        url = 'https://www.ziprecruiter.com/candidate/search?search=' + self.__position + '&location=' + self.__location
        driver.get(url)
        time.sleep(1)
        self.scrape()

    # Find different elements (Job title, location, etc.) and return their values.
    def get_records(self, job_article):
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

    # Scrape the website here.
    def scrape(self):
        # Evade the alert shown in the beginning.
        try:
            el = driver.find_element(By.ID, "createAlertPop")
            action = webdriver.common.action_chains.ActionChains(driver)
            action.move_to_element_with_offset(el, 5, 5)
            action.click()
            action.perform()
        except NoSuchElementException:
            pass
        # Find all the job articles
        jobs_articles = driver.find_elements(By.CLASS_NAME, "job_content")
        # Take every job article, create a job list.
        for job_article in jobs_articles:
            record = self.get_records(job_article)
            job = Job(record[2], record[0], record[1], record[3], '')
            self.__job_list.append(job)
        for job in self.__job_list:
            print(job.__str__())
