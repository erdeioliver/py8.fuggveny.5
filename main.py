'''
5. Feladat
Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír! 
A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvények, amely a lista legkisebb elemével tér vissza. 
A program írja ki, hogy melyik volt a megadott legkisebb szám!
'''

lista = []

def legkisebb(listacska):
    tarolo = listacska[0]
    for i in listacska:
        if i < tarolo:
            tarolo = i
    return print(tarolo)

while True:
    bekeres = int(input("Kérek számokat: "))
    if bekeres < 0:
        break
    lista.append(bekeres)
legkisebb(lista) 