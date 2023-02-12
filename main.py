import re
from functions import *
from random import choice
with open("data.html") as f:
    content=f.readlines()
d={}
for row in content:
    for i in range(1,len(content)-2,3):
        s=content[i]+content[i+1]+content[i+2].replace('white','rgb(255,255,255)')
        result=re.findall("fill: (.*);",s)
        color_fill1=re.search('''"hsl(.*)"''',content[i]).group(1)
        color_fill=color_fill1.replace("(",'').replace(')','').replace("%",'').split(',')
        color_fill=[int(a) for a in color_fill]
        color_name="rgb"+str(hsl_to_ansi(color_fill[0],color_fill[1],color_fill[2],color_fill1,True))
        color_fill=hsl_to_ansi(color_fill[0],color_fill[1],color_fill[2],color_fill1,True)
        d[to_rgb(color_fill[0],color_fill[2],color_fill[1],color_name)]=result
print(to_rgb(255,0,0,"OUTPUT >>>>>"))
l=list(d.keys())
print(d)
print(show(d))
truth=[False for i in range(len(d.keys()))]
print(show(d))
actual_base=0
shots=0
print(show(d))
move(1,0,d)
print(show(d))
'''
while prod(truth)!=True:
    #trouver les boules pouvant etre bougees
    for i in range(len(l)):
      if d_between_indexes(l[get_white_index(d)[0]],l[i],l)==1:
        if l[i-1] in d[l[i]]:
            print(i,i-1,"TO BE MOVED UPPER")
        elif l[i]==d[l[i-1]]:
            print("TO BE MOVED TOO")
        else:
            move()
    #compteur de coups
    shots+=1
    #verification at each iteration
    for e in d.keys():
        if all_elements_equal(e):
            truth[l.index(e)]=1
    #print(show(d))
print("En",shots,"coups!")
'''