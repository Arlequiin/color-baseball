import re
from functions import *
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
        d[hsl_to_ansi(color_fill[0],color_fill[1],color_fill[2],color_fill1)]=result
print(to_rgb(255,0,0,"OUTPUT >>>>>"))
l=list(d.keys())
print(d)
print(show(d))
truth=[False for i in range(len(d.keys()))]
actual_base=0
shots=0
for a in l:
      if d_between_indexes(l[get_white_index(d)[0]],a,list(d.keys()))==1:
        print(a,"can be moved.")
while prod(truth)!=True:
    #compteur de coups
    shots+=1
    #verification at each iteration
    for e in d.keys():
        if all_elements_equal(e):
            truth[l.index(e)]=1