#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 18:44:29 2021
@author: nirmalpatil
"""
import os
from datetime import date
from datetime import timedelta
from twilio.rest import Client



 
import json
import requests
import pandas as pd
from Job import Job
from bs4 import BeautifulSoup

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
headers = {'Content-Type': 'application/json'}



def apidata(): #optimised for 20 results to be fetched
    url = "https://remotive.io/api/remote-jobs?category=software-dev"
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
    jobs = recent_jobs
    

    jobList = []
    for ind in jobs.index:
        job = Job(jobs['job_title'][ind], jobs['company_name'][ind], jobs['company_location'][ind], jobs['job_description'][ind],jobs['date_posted'][ind])
        jobList.append(job)
            
    for job in jobList:
        print(job.__str__())
        print('****************************************************************************')
    return jobList
    
def send_Message(data):
    

# Your Account SID from twilio.com/console
    account_sid = "ACd5e984dcce56ebbee08c285da6b1ec10"
# Your Auth Token from twilio.com/console
    auth_token  = "d7408dbbde7c43406bbcd3c5b0b00692"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
    to="+17178057287", 
    from_="+17259996504",
    body=data)
    
def main():   
  
    jobs = apidata()
    for i in jobs:
        data = i.__str__()
        send_Message(data);
    
if __name__=="__main__":
    main()
