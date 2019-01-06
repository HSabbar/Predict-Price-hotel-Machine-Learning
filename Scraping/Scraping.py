#!/usr/bin/env python3
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time
import requests

import csv
import re

PageSuivants = []

def download_page(url):
    browser = webdriver.Firefox()
    browser.get(url)
    return browser

def download_pageSOUP(url):
    requete = requests.get(url)
    page = requete.content
    soup = BeautifulSoup(page, 'html.parser')
    return soup

def Init_page(lien):
    driver = download_page(lien)

    likns = []
    parentElement = driver.find_elements_by_class_name("bodycon_main")
    elementList = parentElement[0].find_elements_by_tag_name("a")

    for item in elementList:
        href = item.get_attribute('href')
        if (likns.count(str(href)) == 0 ) & (href != lien) & (len(href) > 90) & (href.find('#REVIEWS') < 0): 
            likns.append(href)
            # print (href)
        if len(href) == 86:
            PageSuivants.append(href)

    driver.quit()
    return likns

with open('Donne.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, quotechar=' ', quoting=csv.QUOTE_ALL)
    # spamwriter.writerow(['Prix', 'Nombre d\'utilisateur','Excellent', 'Très bon','Moyen','Médiocre','Horrible', 'Nombre des étoiles d’hôtel'])

def Scrape_pages(url):
    driver = download_pageSOUP(url)

    h1 = driver.find("h1", id ="HEADING")
    # print(h1.string)
    loca = ""
    for l in driver.find("span", class_="detail"):
        loca += l.string

    # print(str(loca))
    infogenral=""
    nb_etoiles = 0
     
    info = driver.find("div", class_="hotels-hotel-review-overview-HighlightedAmenities__amenities---3sdz")                     
    if(info == None):
        info = driver.find("div", class_="hotels-hotel-review-about-with-photos-AmenityGroup__amenitiesList--1kgjY")

    for inf in info.descendants:
        if (inf.string != None) & (infogenral.count(str(inf.string)) == 0) & ( len(re.findall(r'\d+', str(inf.string))) == 0) :
            infogenral += str(inf.string) + ", "

        if re.findall(r'\d+', str(inf.string)):
            nb_etoiles = re.findall(r'\d+', str(inf.string))[0]

    # print(infogenral)
    # print(nb_etoiles)

    avis = ""
    av = driver.find("span", class_="reviews_header_count")
    for a in av.descendants:
        if (a.string != None) & (avis.count(str(a.string)) == 0):
            avis += str(a.string)

    if len(re.findall(r'\d+', avis)) == 2:
        nb_uti = re.findall(r'\d+', avis)[0] + re.findall(r'\d+', avis)[1]
    else:
        nb_uti = re.findall(r'\d+', avis)[0]

    # print(nb_uti)

    Excell = ""
    exce = driver.find("span", class_="row_num ")
    for a in exce.descendants:
        if (a.string != None) & (Excell.count(str(a.string)) == 0):
            Excell += str(a.string)

    if len(re.findall(r'\d+', Excell)) == 2:
        nb_Ex = re.findall(r'\d+', Excell)[0] + re.findall(r'\d+', Excell)[1]
    else:
        nb_Ex = re.findall(r'\d+', Excell)[0]
    # print(nb_Ex)

    tbon = ""
    pousa = ""
    avvv = driver.find("ul", class_="common-ratings-histogram-Histogram__ratings_chart--4sIkK")
    for a in avvv.descendants:
        if (a.string != None) & (pousa.count(str(a.string)) == 0):
            pousa += str(a.string) + '\n'


    tb = driver.find("div", class_="prw_rup prw_filters_detail_checkbox")
    # print(tb)
    for a in tb.descendants:
        if (a.string != None) & (tbon.count(str(a.string)) == 0):
            tbon += str(a.string) + '\n'

    # print(tbon)
    suprAvis = []
    suprAvis = re.findall(r'\d+', str(pousa))

    if len(suprAvis) < 5:
        for x in range(len(suprAvis),5):
            suprAvis.append(0)


    # print(suprAvis)

    prix = driver.find("div", class_="ui_columns is-mobile is-multiline is-vcentered is-gapless-vertical dominantOfferBlock")


    if prix == None:
        prix = driver.find("div", class_= "premium_offers_area offers linkStrategyBlackPriceHover offsiteArrowPartner offsiteControlOrder")
        if prix == None:
            prix = driver.find("div", class_= "ui_columns is-gapless is-mobile")
    
    prixf = []
    for p in prix.descendants:  
        if (p.string != None) & (prixf.count(str(p.string)) == 0) :
            prixf += re.findall(r'\d+', str(p.string))
    
    # print(prixf[0]) 
    catprix = 0
    if int(prixf[0]) < 80:
        catprix = 1
    elif (int(prixf[0]) >= 80) & (int(prixf[0]) < 120):
        catprix = 2
    else:
        catprix = 3

    with open('Donne.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow([prixf[0], nb_uti, suprAvis[0], suprAvis[1], suprAvis[2], suprAvis[3], suprAvis[4], nb_etoiles, catprix])

if __name__ == "__main__":
    lien1 = "https://www.tripadvisor.fr/Hotels-g187147-Paris_Ile_de_France-Hotels.html#"
    PageSuivants.insert(0, lien1)
    for lienI in PageSuivants:
        print(lienI)
        for fre in Init_page(lienI):
            print(fre)
            Scrape_pages(fre)

        print(PageSuivants)

