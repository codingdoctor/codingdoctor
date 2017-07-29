#!/usr/bin/env python
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np
from pandas import DataFrame, Series

html = urlopen('http://www.mjh.or.kr/index.php?mid=page_wOcF10')
source = html.read()
html.close()

### BeautifulSoup 으로 parsing

soup = BeautifulSoup(source, "lxml")
list_per_doctors = soup.find_all('tr', {'class': 'timetablePerDoctor'})
list = [None] * len(list_per_doctors)

for n in range(len(list_per_doctors)):
    list[n] = [None] * 15
    list_td = list_per_doctors[n].find_all('td')
    dept = list_per_doctors[n].find_all('td', {'class': 'oddTdss'})
    if dept:
        list[n][0] = dept[0].text
        for item in range(1,len(list_td)):
            list[n][item] = list_td[item].text
    else:
        list[n][0] = list[n-1][0]
        for item in range(0,len(list_td)):
            list[n][item+1] = list_td[item].text
    # print(list[n])


### Pandas 로 정리


index_number = ['1','2','3','4','5','6','7','8',
    '9','10','11','12','13','14','15']
df = DataFrame(np.array(list), columns=pd.Index(index_number))
print(df)

### CSV 로 저장
index_list=['Department', 'Doctor', 'Selective', 'Mon_AM', 'Mon_PM',
    'Tue_AM', 'Tue_PM', 'Wed_AM', 'Wed_PM', 'Thu_AM', 'Thu_PM',
    'Fri_AM', 'Fri_PM', 'Sat_AM', 'Specialty' ]
df = DataFrame(np.array(list), columns=pd.Index(index_list))
# df.to_csv('output.csv', encoding='utf-8')
