import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://kulliye.karabuk.edu.tr/"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

allpage = page_soup.findAll("div",{"class":"post medium-post"})
print(allpage[0].img['src']) # görsel linki
print(allpage[0].li.text) #haber tarihi
print(allpage[0].h2.text) # Haber başlığı
print(allpage[0].a['href']) # haber linki

token = "1423255491:AAEujUpmOGcoAGAO-ltM-As4qB2qhk83CBY"  # telegram token
chat_id = "1423255491"  # telegram id

# print(allpage[0].text + "https://muh.karabuk.edu.tr/"+allpage[0].a['href'] + "\n" +  allpage[1].text + "https://muh.karabuk.edu.tr/"+allpage[1].a['href'])

# # # Duyuru Baslik
# for i in allpage:
#     requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 698212163, 'text': (i.text + "https://muh.karabuk.edu.tr/"+i.a['href'])}).json()
    # requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 698212163, 'text': ("https://muh.karabuk.edu.tr/"+i.a['href'])}).json()
    # print(i.text,"https://muh.karabuk.edu.tr/"+i.a['href'])






