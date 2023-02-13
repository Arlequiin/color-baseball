import re
from functions import *
from random import *
import time
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
truth=[[False for i in range(3)] for i in range(len(l))]
actual_base=0
shots=0
chosen_base=1
print(truth)
while not prod(prod(sub_truth) for sub_truth in truth):
    #trouver les boules pouvant etre bougees
    iw,jw=get_white_index(d)
    print(iw,chosen_base)
    if d_between_indexes(l[iw],l[chosen_base],l)==1:
        for i in range(2):
               move(chosen_base,i,d)
               if chosen_base<4:
                 chosen_base+=1
               else:
                chosen_base=0

        
    
    #compteur de coups
    shots+=1
    print(shots,"coups")
    #verification at each iteration
    for e in d:
        if all_elements_equal(e):
            truth[l.index(e)]=1
    print(show(d))
    time.sleep(0.5)
print("En",shots,"coups!")