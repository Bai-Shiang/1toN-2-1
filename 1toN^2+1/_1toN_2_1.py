# -*- coding: utf-8 -*-
def _sum(g):
    return g*g+1

a=int(input('plase enter diameter'))
s=0
for x in range(a): 
   s=s+_sum(x)     

print(s)