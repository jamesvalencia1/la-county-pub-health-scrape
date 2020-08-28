# -*- coding: utf-8 -*-
"""
@author: James Valencia
"""

# Import Modules
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Pull Data
NewsURL = 'http://publichealth.lacounty.gov/phcommon/public/media/mediapubhpdetail.cfm?prid=2615'
resp = requests.get(NewsURL)
txt = resp.text
soup = BeautifulSoup(txt, 'lxml')

city_list = []
for x in soup.find_all('li'):
    city_list.append(x.getText().strip())

city_list = list(filter(None, city_list))


# Convert to Dataframe
df = pd.DataFrame(city_list)

# Data Cleansing
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

# Putting it all together
df_final = df1.append(df2)
df_final = df_final.append(df3)
df_final = df_final.rename(columns={0:"City", 1:"Cases"})
df_final = df_final.reset_index(drop=True)

# Removing variables
del df, df1, df2, df3, resp, txt, NewsURL

# Create Excel File
df_final.to_excel("citycases.xlsx")