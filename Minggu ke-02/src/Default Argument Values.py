#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# In[2]:


i = 5

def f(arg=i):
    print(arg)

i = 6
f()


# In[3]:


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# In[4]:


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# In[ ]:




