from bs4 import BeautifulSoup
import requests
import csv
from time import sleep
from random import randint
from datetime import datetime
from Job import Job
import re

def getUrl(position, location):
        template = 'https://www.indeed.com/jobs?q={}&l={}'
        url = template.format(position, location)
        return url
    
def getRecord(card):
    '''Extract job date from a single record '''
    try:
        job_title = card.find('div').find_all('span')
        for title in job_title:
            if 'title' in (str(title)):
                job_title = title.text
        if(job_title is None):
            job_title = ''
    except AttributeError:
        job_title = ''
    try:
        company_name = card.find('span',{'class':'companyName'}).text
        if(company_name is None):
            company_name = ''
    except AttributeError:
        company_name = ''
    try:
        company_location = card.find('div',{'class': 'companyLocation'}).text
        if(company_location is None):
            company_location = ''
    except AttributeError:
        company_location = ''
    try:
        job_summary = card.find('div', {'class': 'job-snippet'}).text
        if(job_summary is None):
            job_summary = ''
    except AttributeError:
        job_summary = ''
    return (job_title, company_name, company_location, job_summary)

def scrape(position, location):
    # Run the main program reouting
    records = []  # creating the record list
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
    }

    url = getUrl(position, location)  # create the url while passing in the position and location.
    while True:
        records = []  # creating the record list
        url = getUrl(position, location)  # user inputs location and role
        print(url)
        try: 
            response = requests.get(url.strip(), headers=headers)
        except requests.exceptions.Timeout as err: 
            print(err)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', 'job_seen_beacon')
       
        jobList = []
        for card in cards:
            record = getRecord(card)
            job = Job(record[0], record[1], record[2], record[3])
            jobList.append(job)
            
        for job in jobList:
            print(job.__str__())

def main():
    scrape('data scientist','charlotte nc')   #user input
if __name__=="__main__":
    main()
 