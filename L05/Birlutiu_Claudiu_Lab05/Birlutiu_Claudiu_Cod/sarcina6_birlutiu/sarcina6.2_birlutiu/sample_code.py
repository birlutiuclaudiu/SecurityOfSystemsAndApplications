#!/usr/bin/python3

# XOR two bytearrays
def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))

PT1   = "This is a known message!"                        #delcararea mesajului cunoscut
CT1 = "a469b1c502c1cab966965e50425438e1bb1b5f9037a4c159"  #cifrul in hexa pentru mesajul cunoscut
CT2 = "bf73bcd3509299d566c35b5d450337e1bb175f903fafc159"  #cifrul in hexa pentru mesajul necunoscut

# Convert ascii string to bytearray
P1 = bytes(PT1, 'utf-8')                                  #obtinerea de bytes din sirul de caractere

# Convert hex string to bytearray
C1 = bytearray.fromhex(CT1)                               #obtinerea sirului de bytes din valorile hexa
C2 = bytearray.fromhex(CT2)

P2 = xor(P1, xor(C1, C2))         #aplicarea formulei de determinarea a textului necunoscut
PT2 = P2.decode('utf-8')          #decodarea sirului de bytes la string utf-8
print(PT2)