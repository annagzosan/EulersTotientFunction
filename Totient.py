# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 19:38:47 2021

@author: user
"""

import math

def solve(m):
    total=0
    for i in range(1,m):
        if(math.gcd(i, m)==1):
            total=total+1
    return total



print("φ(1134)=",solve(1134),"   ","φ(2457)=",solve(2457))