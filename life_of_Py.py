#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:04:53 2021

@author: nirmalpatil
"""

import os
from datetime import date
from datetime import timedelta


import time

from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

from Job import Job
#from ziprecruiter import ZipRecruiter
from IndeedScraper import IndeedScraper
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)

#os.chdir('/Users/nirmalpatil/Desktop/CMU/DFP/Project')
os.chdir('C:\\Users\\rohig\\OneDrive\\Documents\\GitHub\\Data_Focused_Python_Project')
 
import json
import requests
import pandas as pd

from bs4 import BeautifulSoup

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
headers = {'Content-Type': 'application/json'}



def apidata_Remotive(role): #optimised for 20 results to be fetched
    url = "https://remotive.io/api/remote-jobs?category="+role.replace(' ','-')
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200: 
        data = json.loads(response.content.decode('utf-8'))
        print(data['jobs'][0])
        print(type(data))
        df1 = pd.json_normalize(data['jobs'])
       
       



    
    jobs1 = df1[['id','title','company_name','candidate_required_location','publication_date']]
    desc= df1['description']
    desc_list = []
    for i in desc:
        desc_list.append(BeautifulSoup(i).get_text())
    jobs1['description'] =  desc_list
    jobs1['publication_date'] =  jobs1['publication_date'].str[:10]

   
    jobs1 = jobs1.rename(columns={'title': 'job_title', 'company_name': 'company_name','candidate_required_location': 'company_location', 'description': 'job_description','publication_date': 'date_posted'})    
 #   jobs2 = jobs2.rename(columns={'title': 'job_title', 'company_name': 'company_name','location': 'company_location', 'description': 'job_description'})    

    yest = date.today()-timedelta(days=1)
    #jobsDF = jobs1.append(jobs2)
   # jobsDF.reset_index(drop=True, inplace=True)
    recent_jobs = jobs1[jobs1['date_posted']==str(yest)]
    jobs1.to_csv('file_name.csv', sep=',')    
    jobs = jobs1.head(20)
    

    jobList = []
    for ind in jobs.index:
        job = Job(jobs['job_title'][ind], jobs['company_name'][ind], jobs['company_location'][ind], jobs['job_description'][ind],jobs['date_posted'][ind])
        jobList.append(job)
            
    for job in jobList:
        print(job.__str__())
        print('****************************************************************************')
    
def apidata_google(role, location): #optimised for 20 results to be fetched
    url = 'https://serpapi.com/search.json?engine=google_jobs&q=' + role + location + '&hl=en&api_key=2606e41895b5d1a39ab40778b4f0050ea268e1eb5ea6a86e16595d4ad438eed9&start=0&num=10'
    response = requests.get(url, headers = headers)
    if response.status_code == 200: 
        data = json.loads(response.content.decode('utf-8'))
        df1 = pd.json_normalize(data['jobs_results'])
    url2 = 'https://serpapi.com/search.json?engine=google_jobs&q=' + role + location + '&num=20&start=20&hl=en&api_key=2606e41895b5d1a39ab40778b4f0050ea268e1eb5ea6a86e16595d4ad438eed9&start=0&num=10'
    response = requests.get(url2, headers = headers)
    if response.status_code == 200:
        data2 = json.loads(response.content.decode('utf-8'))
        df2 = pd.json_normalize(data2['jobs_results'])


    
    jobs1 = df1[['title','company_name','location','description']]
    jobs2 = df2[['title','company_name','location','description']]
    jobs1 = jobs1.rename(columns={'title': 'job_title', 'company_name': 'company_name','location': 'company_location', 'description': 'job_description'})    
    jobs2 = jobs2.rename(columns={'title': 'job_title', 'company_name': 'company_name','location': 'company_location', 'description': 'job_description'})    


    jobsDF = jobs1.append(jobs2)
    jobsDF.reset_index(drop=True, inplace=True)

    jobsDF.to_csv('file_name.csv', sep=',')    
    
    

    jobList = []
    for ind in jobsDF.index:
        job = Job(jobsDF['job_title'][ind], jobsDF['company_name'][ind], jobsDF['company_location'][ind], jobsDF['job_description'][ind], '')
        jobList.append(job)
            
        for job in jobList:
            print(job.__str__())
            print('****************************************************************************')

def scrape_indeed(role, location):

    indeed = IndeedScraper(role, location)
    indeed.scrape(role, location)
    jobList = indeed.getJobList()
    jobsDF = pd.DataFrame((job.getJobTitle(), job.getCompanyName(), job.getCompanyLocation(), job.getJobDescription()) for job in jobList)
    print(jobsDF)
    for job in jobList:
        
        print(job.__str__())
        print('****************************************************************************')
    
    
    

def main():   
    while(True):
        choice = int(input("""
1: See Jobs from Serpapi (GOOGLE JOBS API). 
2: See Jobs from  Remotive (Remote ONLY)  (Remotive PI). 
3: See Jobs from Indeed (Webscraping). 
4: See Jobs from ZipRecruiter (Webscraping). 
5: See All Jobs. 
6: See Industry insights
Please enter your choice: """))
        if choice == 2 :
            role = input('Enter the role: ')
            apidata_Remotive(role)
        elif choice == 1:
            role = input('Enter the role: ')
            location = input ('Enter the location: ')
            apidata_google(role,location)
        elif choice == 4:
            role = input('Enter the role: ')
            # location = input ('Enter the location: ')
            # zp =  ZipRecruiter()
            # zp.get_url(role,location)
            # zp.search_dir()
        elif choice == 3:
            role = input('Enter the role: ')
            location = input ('Enter the location: ')
            scrape_indeed(role, location)
    
    
    
   
      
    
        
    
    
if __name__=="__main__":
    main()