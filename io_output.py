# with open("plik.txt","r") as plik:
#     content=plik.read()
# print(content)

lista=list(range(30))
with open("plik.csv","a") as plik:
    for i in lista:
        plik.writelines(f"{i};")
    plik.write("\n")