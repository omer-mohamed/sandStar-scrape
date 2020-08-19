import requests
import json
import urllib.request
from bs4 import BeautifulSoup

def scrape_product(content,index):
    if(index == 38 or index == 39):
        return
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

    img = soup.findAll("div", {"class":"overlay-container"})
    img = "http://www.sandstaruae.com/"+img[0].img['src']
    if index<=37:
        urllib.request.urlretrieve(img, "./product img/%d.jpg" % index)
        img_link = "./product img/%d.jpg" % index
        print(img_link)
        
    print(name,category, details)

for i in range(1,41):
    URL = 'http://www.sandstaruae.com/productdetails.aspx?pid={}'.format(i)
    page = requests.get(URL)
    scrape_product(page.content,i)