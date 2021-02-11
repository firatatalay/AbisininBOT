import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://www.karabuk.bel.tr/otobus-saatleri2.asp?hid=15"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

duraklar = page_soup.findAll("div", {"class": "entry_content"})
saatler = page_soup.findAll("a", {"class": "btn"})

print(duraklar[0].text)


# s = "0"
# durak_index = 0
# for i in duraklar:
#     print(i.text)
#     durak_index = durak_index + 1
#     for saat in saatler:
#         s_prev = s
#         s = saat.text.split(':')[0]
#         if int(s) < int(s_prev):
#             durak_index -= 1
#             if durak_index == -1:
#                 break
#         if durak_index == 0:
#             print(saat.text)