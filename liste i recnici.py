# -*- coding: utf-8 -*-
niska="Milena je sinoć videla Mitra, nežnog, zelenog skakavca ispred stacionara i uzviknula je: \"Ju, Mitre, uplašio si me!\". Ali Mitar se na to nije obazirao - žustro je skočio u Mileninom pravcu. Videvši to, Milena polete preko dvorišta i polete ka stacionaru brzinom svetlosti. Nažalost, svetlost je brža od automatskog mehanizma za otvaranje vrata. I tako ostade Milenin trag na ulaznim vratima IS Petnica."
niska=niska.lower ()
reci = niska.split (" ")

reci[4]=reci[4][:-1]
print(reci[14][0:-1])

print(reci[33])
print(reci[33] [0:-1])


telefonski_imenik = {"Paja Patak": 123456, "Mini Maus": 234567, "Šilja": 345678}
vukajlija = {"sojanica": "Posna pljeskavica. Garantovano bez trihinele.", "jahanje": "Omiljena aktivnost šefova za koju je potrebno da radnik ima konjske živce.", "šef": "Čovek koji nema smisao za umor."}
vrste_reči = {"imenice": ["polaznik", "seminar", "lingvistika", "Isidora"], "glagoli": ["slušati", "crtati", "jesti"], "zamenice": ["on", "ona", "ono"]}
print (telefonski_imenik["Mini Maus"])
print(vukajlija["šef"])
print (telefonski_imenik)
vukajlija["šef"]= "Miloš"
print (vukajlija)
print(vukajlija["šef"])


print(vrste_reči.keys())
print(vrste_reči.values())
print(vrste_reči["imenice"][2])

del telefonski_imenik["Mini Maus"]
print (telefonski_imenik)