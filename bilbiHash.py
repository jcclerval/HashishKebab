# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 19:14:56 2018

@author: Jean-Christophe
"""

def getScore(a,b,x,y):
    return (abs(y-b) + abs(y-x))
    
    
if __name__ == '__main__':
    
    print getScore(0,0,1,2)