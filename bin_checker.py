import requests
import pandas as pd
import time as t
import lxml as l
from bs4 import BeautifulSoup
import random as r
from tqdm import tqdm

# numbers = pd.read_excel(r'excel_file_path')['BIN']
numbers = [467123, 593588]


def download_data_from_web(numbers):
    bin_list = []
    for number in tqdm(numbers):
         url = 'https://bincheck.io/details/' + str(number)
         data = requests.get(url).text
         soup = BeautifulSoup(data, features= 'html.parser')
         table = soup.find('table', class_='w-full table-auto')
         table_body = table.find('tbody')
         row4 = table_body.find_all('tr')[4]
         cell4 = row4.find_all('td')[1].text
         bin_list.append(cell4)
         t.sleep(r.randint(2,6))
    df = pd.DataFrame({'bin': numbers,  'bank': bin_list})
    return df

df = download_data_from_web(numbers)
print(df)


