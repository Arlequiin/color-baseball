import time
from functions import *
from random import randint
n=10**6
l=[randint(0,n) for i in range(n)]
def find_median(l):
    n = len(l)
    if n % 2 == 0:
        middle1 = l[n//2 - 1]
        middle2 = l[n//2]
        median = (middle1 + middle2)//2
    else:
        median = l[n//2]
    return median
start=time.time()
def dichotomie(L,e):
    while len(L)>1:
        if e==L[len(L)//2]:
            return True
        elif e>L[len(L)//2]:
            L=L[len(L)//2:]
        else:
            L=L[:len(L)//2]
    return L[0]==e
print(dichotomie(l,n))
end=time.time()
print(to_rgb(0,255,0,("Dichotomie",end-start)))
start=time.time()   
def recherche_seq_triee(L,e):
    L.sort()
    if L[0]<=e<=L[-1]:
        for i in L:
            if i==e:
                return True
            elif e<i:
                return False
    else:
        return False
print(recherche_seq_triee(l,n))
end=time.time()
print(to_rgb(0,255,0,("Recherche seq triee",end-start)))
start=time.time()
def recherche_seq(L,e):
    for i in L:
        if i==e:
            return True
    return False
print(recherche_seq(l,n))
end=time.time()
print(to_rgb(0,255,0,("Recherche seq",end-start)))
