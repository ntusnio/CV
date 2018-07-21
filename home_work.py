# Stwórz klasę Grupa (szkolna)
# Grupa szkolna zawiera uczniów
# Uczeń posiada listę stopni
# Stwórz metodę, która obliczy medianę dla średnich ocen wszystkich uczniów
import random

class Grupa:
    def __init__(self,imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko
        self.oceny = [random.randint(3,5),random.randint(3,5),random.randint(3,5)]
    def srednia(self):
        return round(sum(self.oceny)/len(self.oceny)*2)/2

def mediana(lista):
    lista.sort()
    print(lista)
    if len(lista)%2!=0:
        med=lista[len(lista)//2]
    else:
        med=(lista[len(lista)//2-1]+lista[len(lista)//2])/2
    return med

Uczen=[Grupa('Norbert'),
       Grupa('Andrew'),
       Grupa('Grzegorz'),
       Grupa('Karolina Zadroga'),
       Grupa('kpazik'),
       Grupa('lkobylinski'),
       Grupa('Patryk'),
       Grupa('Pawel T'),
       Grupa('PiotrM'),
       Grupa('Tomek Goral')]

lista=[]
for i in Uczen:
    print(i.imie_nazwisko,' '*(16-len(i.imie_nazwisko)),i.oceny,i.srednia())
    lista.append(i.srednia())
print('===============================')
print('mediana:',mediana(lista))
