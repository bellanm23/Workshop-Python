#!/usr/bin/env python
# coding: utf-8

# In[1]:


list(range(3, 6))


# In[2]:


args = [3, 6]
list(range(*args))


# In[3]:


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


# In[4]:


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# In[ ]:




