#!/usr/bin/env python
# coding: utf-8

# In[1]:


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')


# In[ ]:




