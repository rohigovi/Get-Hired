# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:44:45 2021

@author: rohig
"""
class Job:
    def __init__(self, job_title, company_name, company_location, job_description): # Default constructor
        self._job_title = job_title
        self._company_name = company_name
        self._company_location = company_location
        self._job_description = job_description
            
    def getJobTitle(self):
        return self._job_title
    def setJobTitle(self, job_title):
        self._job_title = job_title
    def getCompanyName(self):
        return self._company_name
    def setCompanyName(self,company_name):
        self._company_name = company_name
    def getCompanyLocation(self,text):
        self._content += text
    def setCompanyLocation(self):
        self._content = ''
    def getJobDescription(self):
        self._job_description
    def setJobDescription(self):
        self._job_description
    def __str__(self):
        return self.job_title + ', ' + str(self._company_name) +  ', ' + str(self._company_location) + ', ' + str(self._job_description)
