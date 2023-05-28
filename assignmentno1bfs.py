#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Code for bfs
graph={
    'A':['B','C','E'],
    'B':['D','A','E'],
    'C':['F','G','A'],
    'D':['B'],
    'E':['A','B','D'],
    'F':['C'],
    'G':['C'],
}
def bfs(graph,initial):
    visited=[]
    queue=[initial]
    while queue:
        node=queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours=graph[node]
            for neighbour in  neighbours:
                queue.append(neighbour)
    return visited
print(bfs(graph,'A'))


# In[ ]:




