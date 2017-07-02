# -*- coding: utf-8 -*-
rečnik={"hot" : {"sinonimi": ["warm", "boiling" ],"antonimi" : ["cold", "chilly"]},"wet" :{"sinonimi": ["damp", "moist" ],"antonimi" : ["dry", "scorched"]},"happy" :{"sinonimi": ["cheerful", "upbeat" ],"antonimi" : ["sad", "unhappy"]}}
print(rečnik["hot"]["sinonimi"]) 
print(rečnik["hot"]["antonimi"]) 
print(rečnik["wet"]["sinonimi"]) 
print(rečnik["wet"]["antonimi"])
print(rečnik["happy"]["sinonimi"]) 
print(rečnik["happy"]["antonimi"])
print(rečnik["wet"]["sinonimi"][0]) 
print(rečnik["wet"]["antonimi"][1])
for reč in rečnik.keys():
    
    print("Reč: ", reč) 
    sin = "Sinonimi: "
    ant = "Antonimi: "

    for sinonim in rečnik[reč]["sinonimi"]:
        sin += sinonim + ", "
    print(sin[:-2])

    for antonim in rečnik[reč]["antonimi"]:
        ant += antonim + ", "    
    print(ant[:-2] + "\n")

