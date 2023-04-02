

def drukuj_po_literze(tekst:str="słoń",znak="-"):
    for i in tekst:
        print(i,end=znak)
        
def wyswietl_dwie_zmienne(a,b):
    return f"wartosc a to {a} a wartosc b to {b}"