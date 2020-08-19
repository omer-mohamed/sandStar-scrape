import requests
import json
from bs4 import BeautifulSoup

def scrape_product(content):
    soup = BeautifulSoup(content, 'html.parser')

    name = soup.find('h3') 
    if not name:
        return
    name = name.text

    category = soup.find(class_="breadcrumb") 
    category = category.text.split()[2]

    details = soup.find(class_="blogpost-body") 
    details = str(details.p).replace("<p>","")
    details = details.replace("</p>","")
    details = details.replace("<br/>",",")
    details = details.split(",")

    print(name," ",category," ", details)



for i in range(1,42):
    URL = 'http://www.sandstaruae.com/productdetails.aspx?pid={}'.format(i)
    page = requests.get(URL)
    scrape_product(page.content)
