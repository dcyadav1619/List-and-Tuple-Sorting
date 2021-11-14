#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

# In[23]:


lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lst = sorted(lst, key = lambda x:x[1])
print(lst)


# In[13]:


lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lst.sort(key = lambda x:x[1])
print(lst)


# In[22]:


lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(0, len(lst)):    
    for j in range(len(lst)):    
        if(lst[i][1] < lst[j][1]):    
          temp = lst[j]
          lst[j] = lst[i]
          lst[i] = temp
print(lst)

