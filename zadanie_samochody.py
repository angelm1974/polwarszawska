'''
1. Stwórz listę samochodów, które chciałbyś mieć.
2. Wprowadzać samochody do listy za pomocą inpu
3. Sprawdzaj ile jest samochodów w liście
4. Sortuj samochody po długości nazwy

'''
# Stwórz pustą listę na samochody
samochody = []

# Wprowadzaj samochody do listy za pomocą inputu, dopóki użytkownik nie wpisze 'q'
while True:
    samochod = input("Wpisz nazwę samochodu (lub 'q' aby zakończyć): ")
    if samochod == 'q':
        break
    samochody.append(samochod)

# Sprawdź ilość samochodów w liście
ilosc_samochodow = len(samochody)
print("Liczba samochodów w liście:", ilosc_samochodow)

# Sortuj samochody po długości nazwy
samochody.sort(key=len)
print("Posortowane samochody po długości nazwy:", samochody)