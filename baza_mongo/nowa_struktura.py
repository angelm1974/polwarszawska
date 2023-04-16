
import datetime
from bson import ObjectId
import pymongo

data_aktualna=datetime.datetime.now().strftime("%Y-%m-%d")
godz=datetime.datetime.now().strftime("%H")

 
klient=pymongo.MongoClient("mongodb+srv://student:jTWMdztmNXlnd3DR@cluster0.cddpk.mongodb.net/?retryWrites=true&w=majority")
db=klient["warszawa"]
kolekcja=db["temperatury"]

def aktualizuj(stacja,temp):
    filtr={'stacja': stacja, 'dzien': data_aktualna}   
    klucz_godziny='dane.'+str(godz)
    aktualizujemy={'$set': {'aktualnie':{"godzina": godz, "temp": temp},klucz_godziny:temp},}

    wynik_aktualizacji=kolekcja.update_one(filtr, aktualizujemy,upsert=True)
