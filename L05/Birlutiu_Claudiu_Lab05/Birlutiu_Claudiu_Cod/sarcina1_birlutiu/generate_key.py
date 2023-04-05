#!/usr/bin/env python3

import random
#lista cu elliterele afabetului englez
s = "abcdefghijklmnopqrstuvwxyz"  
#generarea unei liste de litere random de lungimea sirului s 
# =>amestecarea aleatoare a literelor alfabetului
list = random.sample(s, len(s))   
                                  
#o permutare a alafabetului englez
print(''.join(list))


