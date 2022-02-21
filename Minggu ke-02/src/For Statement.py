#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Measure some strings:
from collections import UserString


words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# In[2]:


# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


# In[ ]:




