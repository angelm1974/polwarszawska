def drukuj_po_literze(tekst:str="słoń",znak="-"):
    for i in tekst:
        print(i,end=znak)
    
    
# drukuj_po_literze("krowa","*")
# def licz(x=0,*args):
#     print(f"pierwszy argument to {x}")
#     for arg in args:
#         print(f"kolejny argument to : {arg}")

# def sumuj(*args):
#     suma=0
#     return sum(args)

# print(sumuj(1,2,3,4,5,6,7,8,9,10))
from random import randint


def randint(a,b):
    return "idź spać"

def kwadrat_plus_trzy(x):
    return x**2+3

# print(randint([56546465],20))

print(kwadrat_plus_trzy(5))

y=lambda x:x**2+3
print(y(5))
d_l=lambda x: x.upper()

# print(d_l("słoń"))

# kwadraty=map(lambda x:x+1,range(10))
# print(list(kwadraty))

def funkcja_ogolna(x,fn):
    return fn(x)

# print(funkcja_ogolna(5,lambda x:x**2+3))
# print(funkcja_ogolna("słoń",d_l))
# print(funkcja_ogolna([3,4,5,6,7,8],lambda x: sum(x)))

liczby=[-3,-2,-1,0,1,2,3]
print(sorted(liczby,key=lambda x:abs(x)))


