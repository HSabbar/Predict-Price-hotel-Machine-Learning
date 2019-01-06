#!/usr/bin/env python3
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time
import requests

import csv
import re

import _thread

import threading




def download_page(url):
    browser = webdriver.Firefox()
    browser.set_window_size(100, 90)
    browser.get(url)
    return browser

def download_pageSOUP(url):
    requete = requests.get(url)
    page = requete.content
    soup = BeautifulSoup(page, 'html.parser')
    return soup

f = open("MScraping.txt","w+")

def Init_page():
    driver = download_page("https://www.tripadvisor.fr/Hotels-g187147-Paris_Ile_de_France-Hotels.html")
    likns = []
    parentElement = driver.find_elements_by_class_name("relWrap")

    for x in parentElement:
        elementList = x.find_elements_by_tag_name("a")

    for item in elementList:
        href = item.get_attribute('href')
        # print (href)
        likns.append(href)

    driver.quit()

    return likns


def Scraper_Pages(url):
    driver = download_pageSOUP(url)
    for h1 in driver.find_all("h1"):
        f.write(str(h1.text))
        f.write("\n")

    # for divr in driver.find_elements_by_class_name("ui_columns.is-multiline") :
    #     f.write(str(divr.text))
    #     f.write("\n")

    for p in driver.find_all("p"):
        f.write(str(p.text))
        f.write("\n")
    
    f.write("______________________NOUVEAUX TEXT__________________\n")

def worker():
    """thread worker function"""
    print('Worker')



# for i in range(5):
    
    

if __name__ == "__main__":
    # Init_page()
    # threads = []>
    for url in Init_page():
        f.write("\n "+url+"\n")
        Scraper_Pages(url)

        # for i in range(0,len(Init_page())):
        #     t = threading.Thread(target=Scraper_Pages, args=(url,))
        #     threads.append(t)
        #     t.start()






