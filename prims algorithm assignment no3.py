#!/usr/bin/env python
# coding: utf-8

# In[1]:


code of prim algorithm assignment no.3
INF=9999999
V=5
G=[[0,9,75,0,0],
  [9,0,95,19,42],
  [75,95,0,51,66],
  [0,19,51,0,31],
  [0,42,66,31,0]]
selected=[0,0,0,0,0]
no_edge=0
selected[0]=True
print("edge:Weight")
while(no_edge<V-1):
    minimum=INF
    x=0
    y=0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if((not selected[j])and G[i][j]):
                    if minimum>G[i][j]:
                        minimum=G[i][j]
                        x=i
                        y=j
    print(str(x)+"-"+str(y)+":"+str(G[x][y]))
    selected[y]=True
    no_edge+=1


# In[ ]:




