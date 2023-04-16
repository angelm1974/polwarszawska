import requests as rq
from bs4 import BeautifulSoup as bs

strona="https://sggw.meteo.waw.pl/"

dane=rq.get(strona)
strona_bs=bs(dane.text, 'html.parser')
lista_stron=[]
li_strona=strona_bs.find_all('li',class_='metico')
for li in li_strona:
    lista_stron.append(li.find('a')['href'])

def sprawdz_link(strona_bs,klasa):
    try:
        link=strona_bs.find('div',class_=klasa).find('a')['href']
        return link
    except:
        return 'err'
    
    
temperatury={}    
for strona in lista_stron:
    print(strona)
    dane=rq.get(strona)
    strona_bs=bs(dane.text, 'html.parser')
    linki=sprawdz_link(strona_bs,'plotbox_title')
    if linki=='err':
        linki=sprawdz_link(strona_bs,'plotbox-title')
    else:
        linki=linki.replace(",",".")

    temperatury[strona]=linki

    # linki=strona_bs.find('div',class_='plotbox_title').find('strong').text
    # # linki=linki.replace(",",".")
    # temperatury[strona]=linki
print(temperatury)