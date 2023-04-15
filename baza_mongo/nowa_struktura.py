
import datetime
from bson import ObjectId
import pymongo

data_aktualna=datetime.datetime.now().strftime("%Y-%m-%d")
godz=4
temp=10
dzielnice=['Wola', 'Mokotów', 'Bemowo', 'Białołęka', 'Ursus', 'Praga-Południe', 'Praga-Północ', 'Śródmieście', 'Targówek', 'Wawer', 'Wesoła', 'Wilanów', 'Włochy', 'Żoliborz'] 
 
klient=pymongo.MongoClient("mongodb+srv://student:jTWMdztmNXlnd3DR@cluster0.cddpk.mongodb.net/?retryWrites=true&w=majority")

db=klient["warszawa"]
kolekcja=db["temperatury"]
for dzielnica in dzielnice:
    filtr={'dzielnica': dzielnica, 'dzien': data_aktualna}   
    klucz_godziny='dane.'+str(godz)
    aktualizujemy={'$set': {'aktualnie':{"godzina": godz, "temp": temp},klucz_godziny:temp},}

    wynik_aktualizacji=kolekcja.update_one(filtr, aktualizujemy,upsert=True)
