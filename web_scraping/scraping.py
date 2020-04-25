import requests
from bs4 import BeautifulSoup
import pprint, re
import csv

res = requests.get('https://www.jw.org/en/whats-new/')
soup = BeautifulSoup(res.text, 'html.parser')
article = soup.select('.synopsis h3 > a')
dates = soup.select('.meta.pubDate')
# print((article)[2].get('href'))


def filter_jw(article, dates):
    jw_list = []
    for idx, item in enumerate(article):
        # pub = article[idx].getText().replace('        ', '')
        pub = item.getText().replace('\n', '').replace('       ', '')
        href = item.get('href', None)
        date = dates[idx].getText()
        if ('/en/news/' in href):
            jw_list.append({'Date': date, 'Title': pub, 'Link': href})
    return jw_list

#csv_file = open('jw_scraped.csv', 'w')
pprint.pprint(filter_jw(article, dates))

with open('jw_scraped.csv', 'w') as file:


# What to try:
# 1. output to CSV file
# 2. Output to PostgreSQL, perhaps AWS RDS