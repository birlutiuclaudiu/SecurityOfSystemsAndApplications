#!/usr/bin/env python3

# Run "xxd -p -c 20 rev_sh.o",
# copy and paste the machine code to the following:
# aici este codul pe care l-am regasit in codul masina pentru shellcode
ori_sh ="""
31c050682f656e76
682f62696e682f75737289e3b8342a2a2ac1e018
c1e81850683d313233686363636389e631c05068
35363738686262623d89e1506831323334686161
613d89e231c050535056515289e189e231c0b00b
cd80
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


