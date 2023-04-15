from bson import ObjectId
import pymongo
 

klient=pymongo.MongoClient("mongodb+srv://student:jTWMdztmNXlnd3DR@cluster0.cddpk.mongodb.net/?retryWrites=true&w=majority")

db=klient["warszawa"]

kolekcje=db.list_collection_names()



# for kolekcja in kolekcje:
#     print(kolekcja)

kolekcja=db["temperatury"]

# dodaj nowy dokument do kolekcji
nowy_dokument={'dzielnica': 'Wawer', 'temp': 12.12, 'godzina': 11}
wynik_wstawiania=kolekcja.insert_one(nowy_dokument)
print(wynik_wstawiania.inserted_id)

# def filtr_po_temp(filtr):
#     dokumnety=kolekcja.find(filtr)
#     for dokument in dokumnety:
#         print(dokument)

# for dokument in dokumnety:
#     print(dokument)
    
filtr={'dzielnica': 'Janki'}   

aktualizujemy={'$set': {'wiatr': 133.01, 'temp': 12.12}}

wynik_aktualizacji=kolekcja.update_one(filtr, aktualizujemy,upsert=True)
print(wynik_aktualizacji.modified_count)

# filtr_po_temp({'temp': {'$gt': 10}})