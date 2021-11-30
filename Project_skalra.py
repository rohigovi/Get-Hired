#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 12:54:29 2021

@author: Subhav Kalra
@andrewID: skalra
"""

import json
import requests
import pandas as pd
from Job import Job
    
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
headers = {'Content-Type': 'application/json'}



def apidata(role, location): #optimised for 20 results to be fetched
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
        job = Job(jobsDF['job_title'][ind], jobsDF['company_name'][ind], jobsDF['company_location'][ind], jobsDF['job_description'][ind])
        jobList.append(job)
            
        for job in jobList:
            print(job.__str__())
            print('****************************************************************************')
    
    

def main():
    role = input('Enter the role: ')
    location = input ('Enter the location: ')
    apidata(role,location)
if __name__=="__main__":
    main()
