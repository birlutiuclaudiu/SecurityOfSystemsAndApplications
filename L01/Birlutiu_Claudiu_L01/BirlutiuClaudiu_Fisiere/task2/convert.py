#!/usr/bin/env python3

# Run "xxd -p -c 20 rev_sh.o",
# copy and paste the machine code to the following:
# aici este codul pe care l-am regasit in codul masina pentru shellcode
ori_sh ="""
eb2b5b31c089430c
895b1089431489431c8d4b18894b288943248d4b
20894b2c8943308d4b108d5328b00bcd80e8d0ff
ffff2f7573722f62696e2f656e762a2a2a2a4141
414142424242613d31312a2a2a2a623d32322a2a
2a2a45454545464646464e4e4e4e
"""

sh = ori_sh.replace("\n", "")

length  = int(len(sh)/2)
print("Length of the shellcode: {}".format(length))
s = 'shellcode= (\n' + '   "'
for i in range(length):
    s += "\\x" + sh[2*i] + sh[2*i+1]
    if i > 0 and i % 16 == 15: 
       s += '"\n' + '   "'
s += '"\n' + ").encode('latin-1')"
print(s)


