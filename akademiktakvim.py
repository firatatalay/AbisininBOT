import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://oidb.karabuk.edu.tr/icerikGoster.aspx?K=S&id=40&BA=index.aspx"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

p = page_soup.findAll("p", {"style": "color: rgb(0, 0, 0); font-family: Tahoma; font-size: medium; background-color: rgb(240, 240, 240);"})

print(p[0].text) #Başlık, 0-5 indisler
print("https://oidb.karabuk.edu.tr/"+p[0].a['href']) #pdf yolu 0-5 indisler
