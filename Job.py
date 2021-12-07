# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:44:45 2021

@author: rohig
"""
class Job:
    def __init__(self, job_title, company_name, company_location, job_description, job_date): # Default constructor
        self._job_title = job_title
        self._company_name = company_name
        self._company_location = company_location
        self._job_description = job_description
        self._job_date = job_date
            
    def getJobTitle(self):
        return self._job_title
    def setJobTitle(self, job_title):
        self._job_title = job_title
    def getCompanyName(self):
        return self._company_name
    def setCompanyName(self,company_name):
        self._company_name = company_name
    def getCompanyLocation(self):
        return self._company_location
    def setCompanyLocation(self, company_location):
        self._company_location = company_location
    def getJobDescription(self):
        return self._job_description
    def setJobDescription(self, job_description):
        self._job_description = job_description
    def getJobDate(self):
        return self._job_date
    def setJobDate(self, job_date):
        self._job_description = job_date 
    def __str__(self):
        return '\nJOB DATE:' + str(self._job_date) + '\nJOB TITLE: ' + str(self._job_title) + '\n\nCOMPANY NAME: ' + str(self._company_name) +  '\n\nLOCATION: ' + str(self._company_location) + '\n\nJOB DESCRIPTION: ' + str(self._job_description)