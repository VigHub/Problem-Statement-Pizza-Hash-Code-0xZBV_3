'''
Created on 21 feb 2018

@author: gviga
'''

import numpy as np
import sys
from operator import itemgetter

def fun(h,l):
    lst = []
    for i in range(h,0,-1):
        for j in range(h,0,-1):
            if i*j<=h and i*j>=2*l:
                lst.append("%d %d %d"%(i*j,i,j))
    lst = sorted(lst)
    daRet1=[]
    daRet2=[]
    daRet3=[]
    for el in lst:
        elem = el.split()
        daRet1.append(int(elem[0]))
        daRet2.append(int(elem[1]))
        daRet3.append(int(elem[2]))
        
    return sorted(zip(daRet1,daRet2,daRet3),key=itemgetter(2,0),reverse=True) # higher score
    #return sorted(zip(daRet1,daRet2,daRet3),key=itemgetter(0,2),reverse=True)  #lower score



def leggiPizza(nomeFile): 
    """Prende in input il nome del file da leggere e restituisce la matrice pizza,
    il numero L e il numero H"""
    with open(nomeFile, 'r') as fin:
        R,C,L,H = [int(n) for n in fin.readline().split()]
        pizza = np.zeros([R,C])
        for i in range(R):
            riga = fin.readline()
            for j,c in zip(range(C),riga):
                if c == "T":
                    pizza[i][j] = 1
        fin.close()
        return pizza, L, H

def isGiustoH(pizza,r1,r2,c1,c2,H):
    """Controlla se la fetta di pizza passata in input rispetta la condizione H"""
    if np.isnan(pizza[r1:r2+1,c1:c2+1].size):
        return False
    return pizza[r1:r2+1,c1:c2+1].size<=H 

def isGiustoL(pizza,r1,r2,c1,c2,L):
    """Controlla se la fetta di pizza passata in input rispetta la condizione L"""
    tomato = np.sum(pizza[r1:r2+1,c1:c2+1])
    if np.isnan(tomato):
        return False
    tot = pizza[r1:r2+1,c1:c2+1].size
    mush = tot-tomato
    return mush>=L and tomato>=L

    
def tagliaPizza(pizza,H,L,nomeFiledaScrivere):
    nFette=0
    score=0
    ing_falliti=0
    ing_usato=False
    sFette = [] # lista di strighe per scrivere le righe e le colonne delle fette
    #nFetteVerticali = nFetteOrizzontali = nAltreFette = 0 
    for i in range(pizza.shape[0]):
        for j in range(pizza.shape[1]):
            ing_usato=False
            if(np.isnan(pizza[i][j])):
                continue
            for k0,k1,k2 in fun(H,L):
                if isGiustoH(pizza,i,i+k1-1,j,j+k2-1,H) and isGiustoL(pizza,i,i+k1-1,j,j+k2-1,L) and i+k1<=pizza.shape[0] and j+k2<=pizza.shape[1]:
                    print("Fetta %d" %(nFette+1))
                    nFette+=1
                    print(pizza[i:i+k1,j:j+k2])
                    score+=pizza[i:i+k1,j:j+k2].size
                    print()
                    pizza[i:i+k1,j:j+k2].fill(np.NaN)
                    sFette.append("%d %d %d %d\n" %(i,j,i+k1-1,j+k2-1))
                    print("Score %s"%score)
                    ing_usato=True
                    continue
            if not ing_usato:
                ing_falliti+=1                       
    fout = open(nomeFiledaScrivere,"w")
    fout.write("%d\n"%nFette)
    for i in range(nFette):
        fout.write(sFette[i])
    print("Your score --> %d"%score)
    print("Ingredienti inusati --> %d"%ing_falliti)
    """print("Fette Orizzontali %d"%nFetteOrizzontali)
    print("Fette Verticali %d"%nFetteVerticali)
    print("Altre Fette %d"%nAltreFette)"""
    fout.close()

def main():
    if len(sys.argv) < 3:
        sys.exit('Syntax: %s <filename> <output>' % sys.argv[0])
    [pizza,L,H] = leggiPizza(sys.argv[1])
    tagliaPizza(pizza,H,L,sys.argv[2])
    print(pizza)

if __name__ == '__main__':
    main()
     
    
    
