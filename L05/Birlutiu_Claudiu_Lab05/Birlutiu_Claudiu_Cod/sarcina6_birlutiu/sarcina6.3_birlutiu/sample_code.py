#!/usr/bin/python3

# XOR two bytearrays
def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))


IV_1 = "b8c1226d0517a72f71acf59c98ff9076"   #reprezinta primul IV cu care Bob a codificat mesajul 
CT_1 = "90e620623fa06434e0f71401909d9192"   #mesajul codificat cu ajutorul IV_1
IV_2 = "5b30bedf0517a72f71acf59c98ff9076"   #IV -ul urmator; predictibil
#ideea e sa ghicim ce a zis BOB astfel ca vom prezice daca a spus Yes
Pred_1 = "Yes" #valoare presupusa

# Convert ascii string to bytearray
P1 = bytes(Pred_1, 'utf-8')                #obtinerea de bytes din sirul de caractere

# Convert hex string to bytearray
IV_1_bytes = bytearray.fromhex(IV_1)             #obtinerea sirului de bytes din valorile hexa
IV_2_bytes = bytearray.fromhex(IV_2)
CT_1_bytes =  bytearray.fromhex(CT_1)
#in prima faza vom face un XOR intre predictie si IV_1 folosit de catre Bob
K = xor(P1, IV_1_bytes)
#verificam ce am obtine daca raspunsul al doilea al lui Bob este Yes sau No
#facadn XOr intre rezultatul anterior si IV_2 predictibil
CT_2 = xor(K, IV_2_bytes)
print("Rezultat: ", CT_2.hex())

