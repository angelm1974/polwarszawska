'''
1. Stowrz liste uczestnikow zawodow w taki sposob
aby mogli się do niej zapisać amatorzy, zawodnicy i profesjonaliści
2. W kazdej z grup ma być 3 osoby
3. Każdy zawodnik ma miec następujące dane: 
imie, nazwisko, wiek, najlepszy_czas
4. posortuj zawodników po najlepszym czasie
5. Zapisz dane do pliku zawodnicy.csv
'''


lista_zawodnikow=[]
amatorzy=[]
zawodnicy=[]
prof=[]
amatorzy=[{"imie":"Adam","nazwisko":"Kowalski","wiek":20,"najlepszy_czas":10,"typ":"amator"},
          {"imie":"Ewa","nazwisko":"Nowak","wiek":25,"najlepszy_czas":11,"typ":"amator"},
          {"imie":"Zenon","nazwisko":"Kowalski","wiek":30,"najlepszy_czas":12,"typ":"amator"}]

zawodnicy=[{"imie":"Jan","nazwisko":"Słowik","wiek":20,"najlepszy_czas":8.6,"typ":"zawodnik"},
           {"imie":"Tomek","nazwisko":"Kowalski","wiek":25,"najlepszy_czas":9.5,"typ":"zawodnik"},
           {"imie":"Zdzisław","nazwisko":"Niski","wiek":30,"najlepszy_czas":10.5,"typ":"zawodnik"}]

prof=[{"imie":"Anna","nazwisko":"Rogowska","wiek":20,"najlepszy_czas":5.6,"typ":"profesjonalista"},
      {"imie":"Tomasz","nazwisko":"Myalska","wiek":25,"najlepszy_czas":6.5,"typ":"profesjonalista"},
      {"imie":"Piotr","nazwisko":"Maliniak","wiek":30,"najlepszy_czas":7.5,"typ":"profesjonalista"},]


def sortuj(x):
    return x["najlepszy_czas"]

amatorzy.sort(key=sortuj)
zawodnicy.sort(key=sortuj)
prof.sort(key=sortuj)

lista_zawodnikow.append(amatorzy)
lista_zawodnikow.append(zawodnicy)
lista_zawodnikow.append(prof)

with open("zawodnicy.csv","w") as plik:
    plik.write("imie;nazwisko;wiek;najlepszy_czas;typ\n")
    for i in lista_zawodnikow:
        for j in i:
            for k in j:
                plik.write(str(j[k]))
                plik.write(";")
            plik.write("\n")
    plik.write("\n")