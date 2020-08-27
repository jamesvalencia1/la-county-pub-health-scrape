# -*- coding: utf-8 -*-
"""
@author: James Valencia
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

resp = requests.get('http://publichealth.lacounty.gov/phcommon/public/media/mediapubhpdetail.cfm?prid=2614')
txt = resp.text

soup = BeautifulSoup(txt, 'lxml')
firstb = soup.find_all('b')[0].text


city_list = []
for x in soup.find_all('li'):
    city_list.append(x.getText().strip())

city_list = list(filter(None, city_list))

del resp, txt, firstb

df = pd.DataFrame(city_list)

# Clean-up 

def remove_col(x):
    x = x.drop([2, 3, 4], axis=1)
    return x


## -- Clean up Incorporated Cities
df1 = df[df[0].str.contains('City of')]
df1 = df1[0].str.split('\t', expand=True)
df1 = remove_col(df1)

## -- Clean up Los Angeles Cities
df2 = df[df[0].str.contains('Los Angeles -')]
df2 = df2[0].str.split('\t', expand=True)
df2 = remove_col(df2)

## -- Clean up Unincorporated Cities
df3 = df[df[0].str.contains('Unincorporated -')]
df3 = df3[0].str.split('\t', expand=True)
df3 = remove_col(df3)

df_final = df1.append(df2)
df_final = df_final.append(df3)