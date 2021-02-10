import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://www.havadurumu15gunluk.net/havadurumu/karabuk-hava-durumu-15-gunluk.html"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

tarih = page_soup.findAll("td",{"width":"75"})
print(tarih[0].text)
gun = page_soup.findAll("td",{"width":"70"})
print(gun[0].text) #+1 olarak gidecek 0-2-4
aciklama = page_soup.findAll("div",{"align":"left"})
print(aciklama[4].text) #4'ten itibaren sırasıyla devam ediyor
derece = page_soup.findAll("td",{"width":"45"})
print(derece[0].text,"/"+ derece[1].text) #ikili olarak devam ediyor



