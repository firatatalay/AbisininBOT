import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://karabuk.eczaneleri.org/"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

allpage = page_soup.findAll("li",{"class":"active"})
# print(allpage[1].a.text)
alert = page_soup.findAll("div",{"class":"alert alert-warning"})
# print("\n")
# print(alert[1].text)

containers = page_soup.findAll("div", {"class" : "media-body"})

# print(containers[6].text.split("\n\n\r\n\r\n")[1].strip())
# print("-------")
# print(containers[7].text)
# print("-------")
# print(containers[8].text)
# print("-------")
# print(containers[9].text)
# print("-------")
# print(containers[10].text)
# print("-------")
# print(containers[11].text)

token = "1423255491:AAEujUpmOGcoAGAO-ltM-As4qB2qhk83CBY" #telegram token
chat_id = "1423255491" #telegram id

requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 698212163, 'text': (allpage[1].a.text+", ")  + (alert[1].text)}).json()
# # requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 698212163, 'text': alert[1].text}).json()
#
for i in range(6,12):
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 698212163, 'text': (containers[i].h4.text) + (containers[i].text.split("\n\n\r\n\r\n")[1].strip()) + "\n\n"}).json()


# requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 698212163, 'text': containers[6].text}).json()
# requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 698212163, 'text': containers[7].text}).json()
# requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 698212163, 'text': containers[8].text}).json()
# requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 698212163, 'text': containers[9].text}).json()
# requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 698212163, 'text': containers[10].text}).json()
# requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 698212163, 'text': containers[11].text}).json()