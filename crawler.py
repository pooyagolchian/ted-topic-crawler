# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import lxml

local_path = '/home/pooya/files/doc/o/'
path_format = '.txt'
html_selector ='div.media__message a.ga-link'
page_num = range(1,10)
with open('data.txt', 'r') as headers:
    header = headers.read().splitlines()
    for h in header:
        for count in page_num:
            urlPage = "http://www.ted.com/talks?page=" + str(count) + "&topics%5B%5D=" + h
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