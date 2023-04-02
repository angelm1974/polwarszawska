# liczby=[]
# for liczba in range(1,11):
#     liczby.append(liczba)
# print(liczby)

# liczby=[x**2 for x in range(1,21) if x% 3==0]
# print(liczby)
# lista1=[(x,y) for x in range(1,10) for y in range(1,10)]
# lista1=[[j for j in range(10)] for i in range(4)]
# lista1=[[[chr(x),y]  for x in range(65,73)]for y in range(8,0,-1)]
# for i in lista1:
#     print(i,end="\n")

tekst='''
Dostęp do wody pitnej w Polsce wynosi tylko 1400 m3 wody na mieszkańca, podczas, gdy średnia światowa to 5 tys. m3. W Polsce borykamy się też z nawalnymi deszczami i okresowymi suszami.
Jak mądrze regulować dostęp do zasobów wody? Z okazji Światowego Dnia Wody zapytaliśmy o to ekspertów firmy Kärcher oraz Fundacji Aeris Futuro, którym towarzyszyliśmy z kamerą w czasie budowy ogrodu deszczowego.
Ogród deszczowy to prosty i przyjazny dla środowiska sposób na zagospodarowanie wody opadowej zarówno tej, która trafia do ogrodu za sprawą deszczu, jak i tej z dachów, chodników, ulic, podjazdów i innych utwardzonych powierzchni. Jest też prosty w wykonaniu i łatwy w pielęgnacji.
To też dobry sposób, by zadbać o nasze portfele w duchu ekologiki, bo na podlanie 1 m2 ogrodu zużywamy średnio 2,5 litra wody. Zapewnienie roślinom właściwego nawodnienia w ogrodzie o powierzchni 100 m2, może nas kosztować nawet 900 zł rocznie! Niewielkich rozmiarów zbiorniki retencyjne w postaci rabat z roślinami hydrofitowymi na naszej własnej działce to sama oszczędność.
Zobaczcie nasz film, jak łatwo wykonać samemu ogród deszczowy. Pomogą wam w tym nasi eksperci:
Marek Piątkowski oraz Bartłomiej Oleszko z Fundacji Aeris Futuro, Natalia Bała i Mateusz Stachowicz z firmy Kärcher oraz dr Tomasz Jeleński z Politechniki Krakowskiej.
'''
# tekst=tekst.lower().replace(".","").replace(",","").split()
# set1={x for x in tekst if len(x)>3}
# print(set1)

osoby={"Adam": 23, "Ewa": 22, "Zenon": 33}
imiona={ wartosc:klucz for (klucz, wartosc) in osoby.items()}
print(imiona)