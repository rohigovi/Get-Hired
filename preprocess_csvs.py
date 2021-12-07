# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:35:36 2021

@author: rohig
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\rohig\\OneDrive\\Documents\\GitHub\\Data_Focused_Python_Project')
quarter1_DF = pd.read_excel('data\\allhlcn211.xlsx')
quarter2_DF = pd.read_excel('data\\allhlcn212.xlsx')

quarter1_statewide_DF = quarter1_DF[quarter1_DF['Area'].str.contains("-- Statewide")]
quarter2_statewide_DF = quarter2_DF[quarter2_DF['Area'].str.contains("-- Statewide")]
quarter1_statewide_DF.to_csv('data\\Quarter1_StateWide.csv')
quarter2_statewide_DF.to_csv('data\\Quarter2_StateWide.csv')