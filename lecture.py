# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 18:52:11 2018

@author: Jean-Christophe
"""

#with open('README.md','r') as raw_exemple:

def read(entryFile):
    with open(entryFile,'r') as raw_exemple:
       data = raw_exemple.read().split('\n')
       entry = data[0].split(' ')                              # Entrée dans le code
       print entry
       R = entry[0]
       C = entry[1]
       F = entry[2]
       N = entry[3]
       B = entry[4]
       T = entry[5]
    
    return [R, C, F, N, B, T]
   
if __name__ == '__main__':
    
    entryFile = 'input_data/a_example.in'
    sortie = read(entryFile)
    print sortie