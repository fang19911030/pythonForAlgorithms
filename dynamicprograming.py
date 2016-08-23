# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 15:13:59 2016

@author: pengcheng
"""

def moveTower(height, fromPole, toPole, withPole):
    if height>=1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
        
def moveDisk(fp,tp):
    print ("moving disk from",fp,"to",tp)
    

moveTower(3,"A","B","C")    


def recDC(coinValueList,change,knownResults):
    minCoins=change
    if change in coinValueList:
        knownResults[change]=1
        return 1
    elif knownResults[change]>0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c<change]:
            numCoins=1+recDC(coinValueList,change-i,knownResults)
            
        if numCoins<minCoins:
            minCoins=numCoins
            knownResults[change]=minCoins
#    print(knownResults)        
    return minCoins
    

#print(recDC([1,5,10,25],52,[0]*64))

def dpMakeChange(coinValueList,change,minCoins,coinUsed):
    for cents in range (change+1):
        coinCount =cents
        newCoin = 1
        for j in [c for c in coinValueList if c<change]:
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
                newCoin=j
        minCoins[cents]=coinCount
        coinUsed[cents]=newCoin
        
    return minCoins[change]
    
def printCoins(coinsUsed,change):
    coin = change
    while coin>0:
        thisCoin=coinsUsed[coin]
        print(thisCoin)
        coin=coin-thisCoin
        
def main():
    amt=63
    clist=[1,5,10,21,25]
    coinUsed=[0]*(amt+1)
    coinCount=[0]*(amt+1)
    
    print("Making change for",amt,"requires")
    print(dpMakeChange(clist,amt,coinCount,coinUsed),"coins")
    print("They are:")
    printCoins(coinUsed,amt)
    print("The used list is as follows:")
    print(coinUsed)
    
main()
    