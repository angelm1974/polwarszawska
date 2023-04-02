import requests as  req
import urllib.parse as up
import csv
adres="https://nominatim.openstreetmap.org/search/"

with open("dane_prezentacja.csv","w") as pl:
    pl.write("stacja;lat;lon;miasto;temperatura;predkosc_wiatru\n")

    with open("moje_dane.csv","r") as plik:
        dane=csv.reader(plik,delimiter=";")
        for i in dane:
            if i[1]=="stacja":
                continue
            moje_dane=req.get(adres+up.quote(i[1])+"?format=json").json()
            print(moje_dane[0]["lat"],moje_dane[0]["lon"]) 
            pl.write(f'{i[0]};{moje_dane[0]["lat"]};{moje_dane[0]["lon"]};{i[1]};{i[4]};{i[5]}'+"\n")   
