#!/usr/bin/env python
"""
__author__ = Shannon B. , 10/19/16
"""

import os
import sys
from os import path
import urllib.request as req
import bs4
import datetime
import statistics

__version__ = '0.1.0'

'''
# Example date range: 8/19/16 thru 10/19/16
# Example BASEURL: https://www.wunderground.com/history/airport/KSZT/

# APPENDED QUERY:

# 2016/8/19/CustomHistory.html?dayend=19&monthend=10&yearend=2016&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=

# Table format: Title: Weather History & Observations
# Year| Temp. (deg F)| Dew Point (deg F)| Humidity (%)| Sea Level Press. (in)| Visibility (mi)| Wind (mph)| Precip. (in)
# Month | high, avg, low | high, avg, low | etc | etc

# Data to pull: Temperature , Wind Speed, Barometric Pressure (aka Sea Level Press.) -> take avgs. although not ideal
'''

BASE_URL = 'https://www.wunderground.com/history/airport/KSZT/'


def get_page(url):

    page = req.urlopen(url)
    return page


def get_soup(page):

    soup = bs4.BeautifulSoup(page, "lxml")

    return soup


def construct_date_range_query(start_date, end_date):
    """

    :param start_date: mm/dd/yyyy
    :param end_date: may be string or tup? probably dumb but handling either...
    :return: query_string to append BASE_URL
    """

    start_chunks = start_date.split('/')

    if '/' in end_date:
        end_chunks = end_date.split('/')
    else:
        end_chunks = (end_date[0], end_date[2], end_date[1])

    start_year, start_month, start_day = start_chunks
    end_month, end_day, end_year = end_chunks

    query_to_append = r'{}/{}/{}/CustomHistory.html?dayend={}&monthend={}&yearend={}&req_city=&req_state=' \
                      '&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo='.format(
                        start_year, start_month, start_day, end_day, end_month, end_year)

    return BASE_URL + query_to_append


def get_date_range_from_user(*date_range):

    if not date_range:

        end_date = input('Choose an end date to search, use the format yyyy/mm/dd')

    else:

        now = datetime.datetime.now()

        end_year = now.year
        end_month = now.month
        end_day = now.day

        end_date = (end_year, end_month, end_day)

    start_date = input("Choose an start date in the format yyyy/mm/dd")

    return start_date, end_date


def main():

    date_tup = get_date_range_from_user('2016/10/2')

    query_string = construct_date_range_query(*date_tup)

    page_soup = get_soup(query_string)

    print(page_soup, end=' ')

if __name__ == '__main__':
    main()
