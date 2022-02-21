#!/usr/bin/env python
# coding: utf-8

# In[5]:


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# In[6]:


def concat(*args, sep="/"):
    return sep.join(args)


# In[7]:


concat("earth", "mars", "venus")


# In[8]:


concat("earth", "mars", "venus", sep=".")


# In[ ]:




