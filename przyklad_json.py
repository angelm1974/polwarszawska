import requests as  req

adres="https://danepubliczne.imgw.pl/api/data/synop/"

moje_dane=req.get(adres).json()
print(moje_dane[0])

with open("moje_dane.csv","w") as plik:
    # abc=  map(lambda x: (x+";"),list(moje_dane[0].keys()))
    # print(list(abc))
    klucze=moje_dane[0].keys()
    
    for i in klucze:
        plik.write(i)
        plik.write(";")
    plik.write("\n")    
    for i in moje_dane:
        for j in i:
            print(i)
            plik.write(str(i[j]))
            plik.write(";")
        plik.write("\n")


