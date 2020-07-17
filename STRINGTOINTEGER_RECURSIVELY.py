# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 01:19:29 2020

@author: MrMaak
"""


#RECURSIVE IMPLEMENTATION OF
#CONVERTING A STRING TO AN INTEGER

def convert(s,num):
    if len(s)==1:
        return int(s)+ num*10
    num = int(s[0]) + num*10
    return convert(s[1:],num)
    
s="123"
convert(s,0)