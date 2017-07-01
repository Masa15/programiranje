# -*- coding: utf-8 -*-
x = "loš"
y = "Miloš"
z = "dobar"

print(x in y) #print("loš" in "Miloš")
print(z in y) #print("dobar" in "Miloš")

rečenica="Izasao sam napolje."
print ("napolje" in rečenica)
print ("Milos" in rečenica)

lista_brojeva = [1, 2, 2.5]
lista_niski = ["ovo", "je", "lista", "niski", "ova", "lista", "je", "kul"]
lista_svega = [True, "može", "i", "ovo", 5.0, [1, 2, "tri"]]

print(lista_brojeva)
lista_brojeva[2] = 3
print(lista_brojeva)

print(lista_svega)
lista_svega.append("ćušpajz") # dodaje element na kraj liste
print(lista_svega)
lista_svega.insert(2, "brokoli") # dodaje element pod indeks koji je određen (u ovom slučaju pod indeks 2)
print(lista_svega)

print(lista_niski)
skup=set(lista_svega)
print (skup)

