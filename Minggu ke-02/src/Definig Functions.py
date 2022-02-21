#!/usr/bin/env python
# coding: utf-8

# In[11]:


def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    print()


# In[12]:


fib(2000)


# In[13]:


fib


# In[14]:


f = fib


# In[15]:


f(100)


# In[16]:


fib(0)


# In[17]:


print(fib(0))


# In[18]:


def fib2(n): ## Return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0,1
    while a < n:
        result.append(a) # See below
        a,b = b, a+b
    return result


# In[19]:


f100 = fib2(100) # call it


# In[20]:


f100 # Write the result


# In[ ]:




