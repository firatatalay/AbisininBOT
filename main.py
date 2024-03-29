import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from flask import Flask
from flask import request
from flask import Response
from datetime import datetime
import json
import re
from bottoken import token
token = token() #token harici bir dosyadan çekilecek

app = Flask(__name__)

def parse_message(message):
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    firstname = message['message']['from']['first_name']
    date = message['message']['date']
    username = message['message']['from']['username']

    # pattern = r'/[a-zA-Z]{6,7}'
    # ticker = re.findall(pattern, txt)  #mesajdaki komutları filtreler
    #
    # if ticker:
    #     symbol = ticker[0][1:].upper()
    # else:
    #     symbol = ' '
    return chat_id, txt, firstname, username, date

# def joinDuyuru(i):
#     url = "https://muh.karabuk.edu.tr/index.php?page=announcements"
#     uClient = uReq(url)
#     page_html = uClient.read()
#     uClient.close()
#     page_soup = soup(page_html, 'html.parser')
#     allpage = page_soup.findAll("tr", {"align": "left"})
#     return allpage[i].text + "https://muh.karabuk.edu.tr/"+allpage[i].a['href']

# ' '.join(dizi)
# def fonksiyon(i):
# Return i.text...
# '\n'.join(map(fonksiyon, dizi))

# def otobussaatleri(chat_id):
#     print(chat_id)

def onerisikayet(chat_id, txt, username, date, komut):

    if komut == "/oneri":
        with open('Oneri-Sikayet.txt', 'a+') as log:
            log.write(f'ÖNERİ| {username} {chat_id} {datetime.fromtimestamp(date)} : {txt}\n')
    elif komut == "/sikayet":
        with open('Oneri-Sikayet.txt', 'a+') as log:
            log.write(f'ŞİKAYET| {username} {chat_id} {datetime.fromtimestamp(date)} : {txt}\n')
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id, 'text': ("Değerlendirmeniz alındı, teşekkürler.")}).json()

def akademiktakvim(chat_id):
    import requests
    from bs4 import BeautifulSoup as soup
    from urllib.request import urlopen as uReq

    url = "https://oidb.karabuk.edu.tr/icerikGoster.aspx?K=S&id=40&BA=index.aspx"
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')

    p = page_soup.findAll("p", {
        "style": "color: rgb(0, 0, 0); font-family: Tahoma; font-size: medium; background-color: rgb(240, 240, 240);"})

    # print(p[0].text)  # Başlık, 0-5 indisler
    # print("https://oidb.karabuk.edu.tr/" + p[0].a['href'])  # pdf yolu 0-5 indisler

    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id,
                                                                                         'parse_mode': 'markdown',
                                                                                         'text':(f'*{p[0].text}*\n' "https://oidb.karabuk.edu.tr/" + p[0].a['href']+"\n"
                                                                                                 f'*{p[1].text}*\n' "https://oidb.karabuk.edu.tr/" + p[1].a['href']+"\n"
                                                                                                 f'*{p[2].text}*\n' "https://oidb.karabuk.edu.tr/" + p[2].a['href']+"\n"
                                                                                                 f'*{p[3].text}*\n' "https://oidb.karabuk.edu.tr/" + p[3].a['href']+"\n"
                                                                                                 f'*{p[4].text}*\n' "https://oidb.karabuk.edu.tr/" + p[4].a['href']+"\n"
                                                                                                 f'*{p[5].text}*\n' "https://oidb.karabuk.edu.tr/" + p[5].a['href']+"\n"
                                                                                                 )}).json()

def otobussaatleri(chat_id,hatno):
    url = ("https://www.karabuk.bel.tr/otobus-saatleri2.asp?hid="+hatno)
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')

    duraklar = page_soup.findAll("div", {"class": "entry_content"})
    # saatler = page_soup.findAll("a", {"class": "btn"})

    requests.post(url="https://api.telegram.org/bot{0}/sendMessage".format(token),
                  data={"chat_id": chat_id, "text": f'{duraklar[0].text}', "parse_mode": "markdown"}).json()

def havaDurumu(chat_id):
    url = "https://www.havadurumu15gunluk.net/havadurumu/karabuk-hava-durumu-15-gunluk.html"
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')

    tarih = page_soup.findAll("td", {"width": "75"})
    # print(tarih[1].text)
    gun = page_soup.findAll("td", {"width": "70"})
    # print(gun[0].text)  # +1 olarak gidecek 0-2-4
    aciklama = page_soup.findAll("div", {"align": "left"})
    # print(aciklama[4].text)  # 4'ten itibaren sırasıyla devam ediyor
    derece = page_soup.findAll("td", {"width": "45"})
    # print(derece[0].text, "/" + derece[1].text)
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id, 'parse_mode':'markdown',
                                                                                         'text': ("Karabük \n" +
                                                                                                  tarih[0].text +", "+ f'*{gun[0].text}*' +"\n"+ aciklama[4].text +""   + (derece[0].text + " /" + derece[1].text) + "\n\n" +
                                                                                                  tarih[1].text +", "+ f'*{gun[2].text}*' +"\n"+ aciklama[5].text +""   + (derece[2].text + " /" + derece[3].text) + "\n\n" +
                                                                                                  tarih[2].text +", "+ f'*{gun[4].text}*' +"\n"+ aciklama[6].text +""   + (derece[4].text + " /" + derece[5].text)
                                                                                                  )}).json()

def kulliyehaber(chat_id):
    url = "https://kulliye.karabuk.edu.tr/"
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')

    allpage = page_soup.findAll("div",{"class":"post medium-post"})
    # print(allpage[0].img['src'])  # görsel linki
    # print(allpage[0].li.text)  # haber tarihi
    # print(allpage[0].h2.text)  # Haber başlığı
    # print(allpage[0].a['href'])  # haber linki

    InputMediaPhoto = []
    for i in range(7):
        if allpage[i].img['src'].split('.')[-1] in ['jpg', 'jpeg', 'png']:
            InputMediaPhoto.append(
            {
                "parse_mode": "markdown",
                "type": "photo",
                "media": allpage[i].img["src"],
                "caption": f"_{allpage[i].li.text}_\n*{allpage[i].h2.text}* \n" + allpage[i].a["href"]
            }
        )

    # print(allpage[6].img['src'].split('.')[-1])
    requests.post(url="https://api.telegram.org/bot{0}/sendMediaGroup".format(token), data={"chat_id": chat_id, "media":json.dumps(InputMediaPhoto), "parse_mode": "markdown"}).json()

def kbuDuyuru(chat_id):
    url = "https://muh.karabuk.edu.tr/index.php?page=announcements"
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')
    allpage = page_soup.findAll("tr", {"align": "left"})
    # for i in allpage:
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id,
                                                                                         'parse_mode': 'markdown',
                                                                                         'text': (f'*{allpage[0].strong.text}*\n '+"https://muh.karabuk.edu.tr/"+allpage[0].a['href'] +
                                                                                                  f'\n\n*{allpage[1].strong.text}*\n '+ "https://muh.karabuk.edu.tr/"+allpage[1].a['href'] +
                                                                                                  f'\n\n*{allpage[2].strong.text}*\n '+ "https://muh.karabuk.edu.tr/"+allpage[2].a['href'] +
                                                                                                  f'\n\n*{allpage[3].strong.text}*\n '+ "https://muh.karabuk.edu.tr/"+allpage[3].a['href'] +
                                                                                                  f'\n\n*{allpage[4].strong.text}*\n '+ "https://muh.karabuk.edu.tr/"+allpage[4].a['href'] +
                                                                                                  f'\n\n*{allpage[5].strong.text}*\n '+ "https://muh.karabuk.edu.tr/"+allpage[5].a['href'] +
                                                                                                  f'\n\n*{allpage[6].strong.text}*\n '+ "https://muh.karabuk.edu.tr/"+allpage[6].a['href'] +
                                                                                                  f'\n\n*{allpage[7].strong.text}*\n '+ "https://muh.karabuk.edu.tr/"+allpage[7].a['href'] +
                                                                                                  f'\n\n*{allpage[8].strong.text}*\n '+ "https://muh.karabuk.edu.tr/"+allpage[8].a['href'] +
                                                                                                  f'\n\n*{allpage[9].strong.text}*\n '+ "https://muh.karabuk.edu.tr/"+allpage[9].a['href'])}).json()

def nobetciEczane(chat_id):
    url = "https://karabuk.eczaneleri.org/"
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')
    allpage = page_soup.findAll("li", {"class": "active"})
    alert = page_soup.findAll("div", {"class": "alert alert-warning"})
    containers = page_soup.findAll("div", {"class": "media-body"})
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id,
                                                                                         'parse_mode':'markdown',
                                                                                         'text': (f'*{allpage[1].a.text}*' + ", ") + f'*{(alert[1].text)}*'}).json()

    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id,
                                                                                         'parse_mode':'markdown',
                                                                                         'text': ((f'*{containers[6].h4.text}*') + (containers[6].text.split("\n\n\r\n\r\n")[1].strip()) + "\n\n" +
                                                                                                  (f'*{containers[7].h4.text}*') + (containers[7].text.split("\n\n\r\n\r\n")[1].strip()) + "\n\n" +
                                                                                                  (f'*{containers[8].h4.text}*') + (containers[8].text.split("\n\n\r\n\r\n")[1].strip()) + "\n\n" +
                                                                                                  (f'*{containers[9].h4.text}*') + (containers[9].text.split("\n\n\r\n\r\n")[1].strip()) + "\n\n" +
                                                                                                  (f'*{containers[10].h4.text}*') + (containers[10].text.split("\n\n\r\n\r\n")[1].strip()) + "\n\n"+
                                                                                                  (f'*{containers[11].h4.text}*') + (containers[11].text.split("\n\n\r\n\r\n")[1].strip()))}).json()


@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id, txt, firstname, username, date = parse_message(msg)
        # print(chat_id, txt, firstname, username)
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': -505845238, 'text': ("Mesaj:"+txt+ "\n\nGönderen: t.me/"+username+"")}).json()


        kontrol = 0
        dosya = open('kullanicilar.txt','r+')
        for i in dosya:
            if username in i:
               kontrol=1
               break
        if kontrol == 0:
            dosya.write(f'{username} ')
        dosya.close()


        with open('log.txt', 'a+') as log:
            log.write(f'{username} {chat_id} {datetime.fromtimestamp(date)} {txt}\n')

        otobusmu = txt.split(' ')[0]
        hatno = txt.split(' ')[-1]
        # print(txt)
        # print(hatno)
        # print("/otobussaatleri " + hatno)
        # print(otobusmu)

        komut = otobusmu

        if txt == '/start':
            requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id, 'text': ("Hoşgeldin Abisinin,\n /yardim komutunu kullanarak bot hakkında bilgi edinebilirsin.")}).json()
        elif komut == '/sikayet' or komut == '/oneri':
            print(komut, txt)
            onerisikayet(chat_id, txt, username, date, komut)
        elif otobusmu == '/akademiktakvim':
            akademiktakvim(chat_id)
        elif otobusmu == '/otobussaatleri' and hatno.isdigit() == True:
            otobussaatleri(chat_id, hatno)
        elif txt == '/nobetci' or txt == '/eczane' or txt =='/Eczane' or txt == '/nöbetçi' or txt=='/nobetcieczane':
            nobetciEczane(chat_id)
        elif txt == '/duyuru' or txt =='/Duyuru' or txt =='/DUYURU' or txt == '/duyurular' or txt =='duyurular' or txt =='kbü duyuru':
            kbuDuyuru(chat_id)
        elif txt == '/kbuhaber' or txt =='/kulliyehaber' or txt =='/külliye' or txt == '/kbühaber' or txt =='haberkbü' or txt =='/haberler':
            kulliyehaber(chat_id)
        elif txt == '/havaDurumu' or txt =='/hava' or txt =='/havadurumu' or txt =='/HAVADURUMU' or txt =='/durum':
            havaDurumu(chat_id)
        elif txt == '/yardim' or txt == '/yardım' or txt == '/bilgi' or txt == '/help':
            requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id,
                                                                                                 'text': ("/yardim - Bot Nasıl Çalışır? Ne İşe Yarar?\n"
                                                                                                          "/duyuru - Karabük Üniversitesi Duyuruları\n"
                                                                                                          "/haberler - Karabük Üniversitesi Külliye Haberleri\n"
                                                                                                          "/duyuru - Karabük Üniversitesi Duyuruları\n"
                                                                                                          "/akademiktakvim - Karabük Üniversitesi Akademik Takvim\n"
                                                                                                          "/nobetcieczane - Karabük Nöbetçi Eczaneleri\n"
                                                                                                          "/havadurumu - Karabük Hava Durumu\n"
                                                                                                          "/otobussaatleri - Karabük Otobüs Saatleri\n\n"
                                                                                                          "Komutları ile açıklamalardaki bilgilere erişebilirsiniz.\n\n"
                                                                                                          "Botu değerlendirmek için /oneri veya /sikayet komutlarını kullanabilirsiniz. Örneğin '/oneri Bu bir öneridir.' ya da '/sikayet bu bir şikayettir.'")}).json()
        elif txt == '/otobussaatleri' or txt == '/otobüssaatleri' or txt == '/otobüs' or txt == '/otobus' or txt == 'otobüs saatleri':
            requests.post(url='https://api.telegram.org/bot{0}/sendPhoto'.format(token), data={'chat_id': chat_id, 'photo':'https://i.hizliresim.com/ArXlp2.jpg', 'caption':'Kullanacağınız otobüs hattını listeden görüntüleyerek sonraki komutunuzu /otobussaatleri hat_no şeklinde yapabilirsiniz. Örneğin:/otobussaatleri 15' }).json()
        else:
            requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id, 'text': ("Anlamadım, lütfen /yardim komutu ile bot hakkında bilgi alın."), 'parse_mode':'markdown' }).json()
        return Response('Ok', status=200)
    else:
        return '<h1> Abisinin_BOT WebHook Sayfasına Hoşgeldin. </h1>'

if __name__ == '__main__':
    app.run(debug=True)