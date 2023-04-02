mojslownik={
    "temperatura":25,
    "wilgotnosc":50,
    "cisnienie":1000
    }
drugislownik={
    "temperatura":25,
    "naslonecznienie_v":50,
    "naslonecznienie_h":1000,
    "lat":50,
    "lon":1000,
}
mojslownik.update(drugislownik)
print(mojslownik,type(mojslownik))

print(mojslownik.get("tempratura","brak danych"))
print(mojslownik.keys())
print(mojslownik.values())
print(mojslownik.items())

for k,w in mojslownik.items():
    print(k,w)

print(dir(dict))
