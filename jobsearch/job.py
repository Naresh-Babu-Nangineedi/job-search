#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def job_data(url, items):

    titles = []
    links = []
    companies = []
    summaries = []
    dates = []

    res = requests.get(url).content

    soup = BeautifulSoup(res, 'html.parser')

    data = soup.find_all('div', class_='jobsearch-SerpJobCard')

    for i in data:
        title = i.find('h2', class_='title')
        if items[0] in title.text.strip():

            link = title.find('a')

            day = i.find('span', class_='date')

            company = i.find('span', class_='company')

            summary = i.find('div', class_='summary')

            titles.append(title.text.strip())
            companies.append(company.text.strip())
            summaries.append(summary.text.strip())
            dates.append(day.text.strip())
            links.append('https://www.indeed.co.in' + link['href'])

    return (titles, companies, summaries, dates, links)



			