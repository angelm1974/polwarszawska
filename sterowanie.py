# x=int(input("Podaj liczbę: "))
# y=int(input("Podaj liczbę: "))

# if  x>50:
#     #zrób coś
#     print("Liczba jest za duża!")
# elif x==50:
#     print("Liczba jest równa 50!")
#     if x > y:
#         print("x jest większe od y")
#     elif x < y:
#         print("x jest mniejsze od y")      
# else:
    # print("Liczba jest za mała!")

# zwierzeta=["pies","kot","ryba","krowa","koń"]
# for i in zwierzeta:
    # print(f"Zwierzę: {i} ma {len(i)} znaków")      
    
# liczby=list(range(100,0,-2))    


# lista=[]
# for i in liczby:
#     if i<60 and i>40:
#         continue
#     else:
#        lista.append(i)
# print(lista)

numer=1
while True:
    print(numer)
    numer+=1
    znak= input("Naciśnij enter aby kontynuować")
    if znak=='q':
        break