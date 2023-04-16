import requests as rq
import json
from bs4 import BeautifulSoup as bs
import nowa_struktura as ns
 
def read_plotbox(page,opts,num):
    temp = None
    try:
        temp = page.find('div', class_=opts[num-1]).find('strong')
        return temp
    except:
        num += 1
        if num > len(opts):
            return temp
        else:
            temp = read_plotbox(page, opts, num)
            return temp
 
 
URL_PATH = "https://sggw.meteo.waw.pl/"
PLOTBOX_TITLE_OPTS = [
    'plotbox_title',
    'plotbox-title'
]
 
res = rq.get(URL_PATH)
strona_bs = bs(res.text,'html.parser')
linki = strona_bs.find_all('li',class_='metico')
 
link_list = []
for link in linki:
    temporary_link = link.find('a')['href']
    link_list.append(temporary_link)
 
print(link_list)
 
for link in link_list:
    res = rq.get(str(link))
    strona_bs = bs(res.text,'html.parser')
    row_temp = read_plotbox(strona_bs,PLOTBOX_TITLE_OPTS,1).contents
    temp = str(row_temp).replace(',','.')
    ns.aktualizuj(link,temp)