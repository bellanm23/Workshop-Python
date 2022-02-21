#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Break statement
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # Loop fell through withput findong a factor
        print(n, 'is a prime number')


# In[4]:


# Continue statement
for num in range(2,10):
  if num % 2 == 0:
    print("Found an even number", num)
    continue
  print("Found an odd number", num)


# In[ ]:




