pusta_lista=list()
pusta_lista=[]
imiona=['Adam','Ewa','Zenon']

imiona.insert(1,'Tomek')
print(imiona)
print(imiona.sort())
print(sorted(imiona))
imiona.reverse()


def klucz(imie):
    return len(imie)
imiona.sort(key=klucz,)
print(imiona)
print(imiona.index('Ewa'))


# mojedane=imiona[:2].copy()
# mojedane[1]=77
# print(imiona)
# print(mojedane)
# print(imiona)
# lista=[1,2,3,4,5,6,7,8,9,10]

# print(sum(lista))

#tuple

pusta_tupla=tuple()
pusta_tupla=()
tupla=3,9,10
print(tupla[2])
tupla=list(tupla)
tupla[2]=77
tupla=tuple(tupla)
print(type(tupla))
tupla=*tupla[0:2],11
print(tupla)


