import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://muh.karabuk.edu.tr/index.php?page=announcements"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

allpage = page_soup.findAll("tr",{"align":"left"})
print(allpage[0].strong.text)
# print(page_soup)
# print(allpage[0])


#Linkler
# links = page_soup.findAll("a",{"class":"duyuru"})
# for link in links:
#     if link.has_attr('href'):
#         print(link.attrs['href'])

token = "1423255491:AAEujUpmOGcoAGAO-ltM-As4qB2qhk83CBY"  # telegram token
chat_id = "1423255491"  # telegram id
# 1423255491

# print(allpage[0].text + "https://muh.karabuk.edu.tr/"+allpage[0].a['href'] + "\n" +  allpage[1].text + "https://muh.karabuk.edu.tr/"+allpage[1].a['href'])

# # # Duyuru Baslik
# for i in allpage:
#     requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 698212163, 'text': (i.text + "https://muh.karabuk.edu.tr/"+i.a['href'])}).json()
    # requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 698212163, 'text': ("https://muh.karabuk.edu.tr/"+i.a['href'])}).json()
    # print(i.text,"https://muh.karabuk.edu.tr/"+i.a['href'])






