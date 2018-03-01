# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 19:14:56 2018

@author: Jean-Christophe
"""

def getScore(a,b,x,y):
    return (abs(y-b) + abs(y-x))

def getLatestStart(a,b,x,y,s,f):
    distance = getScore(a,b,x,y)
    
    return f - distance
    

    
    
if __name__ == '__main__':
    
    print getScore(0,0,1,2)
    print getLatestStart(0,0,1,2,1,9)