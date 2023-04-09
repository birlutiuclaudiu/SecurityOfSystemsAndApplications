#!/usr/bin/python3

# XOR two bytearrays
def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))


IV_1 = "cdd58a1dc01a104cbaf4bac83e596c34"   #reprezinta primul IV cu care Bob a codificat mesajul 
CT_1 = "7f99ac57d9ff9f55968386b38e9590b9"   #mesajul codificat cu ajutorul IV_1
IV_2 = "5b369a33c01a104cbaf4bac83e596c34"   #IV -ul urmator ca predictie

#ideea e sa ghicim ce a zis BOB astfel ca vom prezice daca a spus Yes
Pred_1 = "No"

# Convert ascii string to bytearray
P1 = bytes(Pred_1, 'utf-8')                #obtinerea de bytes din sirul de caractere

# Convert hex string to bytearray
IV_1 = bytearray.fromhex(IV_1)                               #obtinerea sirului de bytes din valorile hexa
IV_2 = bytearray.fromhex(IV_2)
CT_1 =  bytearray.fromhex(CT_1)
#in prima faza vom face un XOR intre predictie si IV_1 folosit de catre Bob
K = xor(P1, IV_1)
#verificam ce am obtine daca raspunsul al doilea al lui Bob este Yes sau No
#facadn XOr intre rezultatul anterior si IV_2 predictibil
CT_2 = xor(K, IV_2)
#CT_2 =CT_2.hex()  #convertirea la hex
print(CT_1.hex())
print(CT_2.hex())
print(P1.hex())