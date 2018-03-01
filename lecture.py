# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 18:52:11 2018

@author: Jean-Christophe
"""

#with open('README.md','r') as raw_exemple:
with open('input_data/a_example.in','r') as raw_exemple:
   data = raw_exemple.read().split('\n')
   entry = data[0].split(' ')                              # Entrée dans le code
   
   R = entry[0]
   C = entry[1]
   F = entry[2]
   N = entry[3]
   B = entry[4]
   T = entry[5]
   
   