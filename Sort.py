#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 09:49:33 2021

@author: venkateshprasads
"""

#a=[-1,4,5,-6 ,-7 ,9, 8]
#[4,5,,9,8] --4
#[-1,-6,-7] --3
a=[9,5,6,7,1,4,-8,-2]
# 
pos=list (filter(lambda x:x>0, a))

neg=list (filter(lambda x:x<0, a))
pos.sort(reverse=True)
print(pos)
neg.sort(reverse=True)


j=1
for i,x in enumerate(pos) :
    print(i,x)
    neg.insert(i+j,x)
    j=j+1
    print(neg)


x= lambda x,y:x+y

lambda  para : exp 
print(x)

