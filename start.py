message=" witamy w Pythonie"
# print(message)
str1 ="to jest ciąg tekstowy"
str2 = 'to jest ciąg tekstowy'
str3 = 'To jest mój "cytat"'
tekst='''
Dostęp do wody pitnej w Polsce wynosi tylko 1400 m3 wody na mieszkańca, podczas, gdy średnia światowa to 5 tys. m3. W Polsce borykamy się też z nawalnymi deszczami i okresowymi suszami.
Jak mądrze regulować dostęp do zasobów wody? Z okazji Światowego Dnia Wody zapytaliśmy o to ekspertów firmy Kärcher oraz Fundacji Aeris Futuro, którym towarzyszyliśmy z kamerą w czasie budowy ogrodu deszczowego.
Ogród deszczowy to prosty i przyjazny dla środowiska sposób na zagospodarowanie wody opadowej zarówno tej, która trafia do ogrodu za sprawą deszczu, jak i tej z dachów, chodników, ulic, podjazdów i innych utwardzonych powierzchni. Jest też prosty w wykonaniu i łatwy w pielęgnacji.
To też dobry sposób, by zadbać o nasze portfele w duchu ekologiki, bo na podlanie 1 m2 ogrodu zużywamy średnio 2,5 litra wody. Zapewnienie roślinom właściwego nawodnienia w ogrodzie o powierzchni 100 m2, może nas kosztować nawet 900 zł rocznie! Niewielkich rozmiarów zbiorniki retencyjne w postaci rabat z roślinami hydrofitowymi na naszej własnej działce to sama oszczędność.
Zobaczcie nasz film, jak łatwo wykonać samemu ogród deszczowy. Pomogą wam w tym nasi eksperci:
Marek Piątkowski oraz Bartłomiej Oleszko z Fundacji Aeris Futuro, Natalia Bała i Mateusz Stachowicz z firmy Kärcher oraz dr Tomasz Jeleński z Politechniki Krakowskiej.
'''
# print("\tPython")
# print("Python \njest fajny")
imie="Jan"
nazwisko="Kowalski"
imie_nazwisko=imie+" "+nazwisko
print(imie_nazwisko)
imie_nazwisko=f"{ imie } { nazwisko }"
print(imie_nazwisko)

#liczby całkowite
number1=10
number2=12
suma=number1+number2
print(suma)
print(type(suma))
suma =f"suma liczb: {number1} i {number2} wynosi {suma}"
print(suma)
# print(type(suma))

#liczby zmiennoprzecinkowe
a=10
b=10
print(type(a))
print(type(b))
wynik=a/b
print(wynik)
print(type(wynik))

#wiele przypisań
x,y,z=1,True,4.3


#wartości logiczne
print(3>4)
true=True

#wartosc None
x=None
print(x)

#stałe
MAX_LENGTH=1000

print(MAX_LENGTH)