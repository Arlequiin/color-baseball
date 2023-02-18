import random
from functions import to_rgb
#l = [random.randint(1,10) for i in range(10)]

def min_index(liste):
    min_index=0
    for i in range(len(liste)):
        if liste[i]<liste[min_index]:
            min_index=i
    return min_index

l=[1,2,3]
random.shuffle(l)
print(min_index(l))

def swap(l,x,y):
    temp=l[y]
    l[y]=l[x]
    l[x]=temp

def tri(liste,n=0):
    while len(liste)-n>0:
     swap(liste,n,min(liste[n:len(liste)]))
     print(n,liste[n:len(liste)],min(liste[n:len(liste)]))
     n+=1
    return [n,liste]
print(l)
print("----")
print(tri(l))
