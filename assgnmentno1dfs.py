#!/usr/bin/env python
# coding: utf-8

# In[12]:


graph={
    'A':['B','C','E'],
    'B':['A','D','E'],
    'C':['A','F','G'],
    'D':['B'],
    'E':['A','B','D'],
    'F':['C'],
    'G':['C']
}
def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    print(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
    return visited
dfs(graph,'A')


# In[ ]:




