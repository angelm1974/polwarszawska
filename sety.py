set1=set()
set2={"Gdańsk","Gdynia","Sopot", "Gdańsk"}
# print(set2)
tekst='''
Dostęp do wody pitnej w Polsce wynosi tylko 1400 m3 wody na mieszkańca, podczas, gdy średnia światowa to 5 tys. m3. W Polsce borykamy się też z nawalnymi deszczami i okresowymi suszami.
Jak mądrze regulować dostęp do zasobów wody? Z okazji Światowego Dnia Wody zapytaliśmy o to ekspertów firmy Kärcher oraz Fundacji Aeris Futuro, którym towarzyszyliśmy z kamerą w czasie budowy ogrodu deszczowego.
Ogród deszczowy to prosty i przyjazny dla środowiska sposób na zagospodarowanie wody opadowej zarówno tej, która trafia do ogrodu za sprawą deszczu, jak i tej z dachów, chodników, ulic, podjazdów i innych utwardzonych powierzchni. Jest też prosty w wykonaniu i łatwy w pielęgnacji.
To też dobry sposób, by zadbać o nasze portfele w duchu ekologiki, bo na podlanie 1 m2 ogrodu zużywamy średnio 2,5 litra wody. Zapewnienie roślinom właściwego nawodnienia w ogrodzie o powierzchni 100 m2, może nas kosztować nawet 900 zł rocznie! Niewielkich rozmiarów zbiorniki retencyjne w postaci rabat z roślinami hydrofitowymi na naszej własnej działce to sama oszczędność.
Zobaczcie nasz film, jak łatwo wykonać samemu ogród deszczowy. Pomogą wam w tym nasi eksperci:
Marek Piątkowski oraz Bartłomiej Oleszko z Fundacji Aeris Futuro, Natalia Bała i Mateusz Stachowicz z firmy Kärcher oraz dr Tomasz Jeleński z Politechniki Krakowskiej.
'''
tekst=tekst.lower().replace(".","").replace(",","").split()
for slowo in tekst:
    if len(slowo)>3:
        set1.add(slowo)
# print(set1)
A={1,2,3,4,5,6,7}
B={5,6,7,8,9}
# print(A&B)
# print(A.intersection(B))

print(A-B)
print(B-A)
print(A^B)
print(A.difference(B))
print(A.symmetric_difference(B))
A.update(B)
print(A)
A.discard(4)
print(A)