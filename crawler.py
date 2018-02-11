# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import lxml

local_path = '/home/pooya/files/doc/o/'
path_format = '.txt'
html_selector ='div.media__message a.ga-link'
ted_url = "http://www.ted.com/talks?page="
ted_url_etc = "&topics%5B%5D="
page_num = range(1,10)
with open('data.txt', 'r') as headers:
    header = headers.read().splitlines()
    for h in header:
        for count in page_num:
            urlPage = ted_url + str(count) + ted_url_etc + h
            response = requests.get(urlPage)
            if response:
                data = response.text
                soup = BeautifulSoup(data, 'lxml')
                titles = soup.select(html_selector)
                if titles:
                    for title in titles:
                        output = title.text.encode('utf-8').strip()
                        path = local_path + h + path_format
                        f = open(path, "a")
                        f.write(output + "\r\n")
                        f.close()