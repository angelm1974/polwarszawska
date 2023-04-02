import requests as  req

adres="https://danepubliczne.imgw.pl/api/data/synop/"

moje_dane=req.get(adres)
print(moje_dane)