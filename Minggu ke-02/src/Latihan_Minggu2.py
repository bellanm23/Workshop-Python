#!/usr/bin/env python
# coding: utf-8

# ***
# # 4.1 If Statement
# ***

# In[1]:


x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# ***
# # 4.2 For Statement
# ***

# In[2]:


# Measure some strings:
from collections import UserString


words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# In[3]:


# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


# ***
# # 4.3 Range()
# ***

# In[4]:


for i in range(5):
  print(i)


# In[5]:


list(range(5,10))


# In[6]:


list(range(0, 10,3))


# In[7]:


list(range(-10, -100, -30))


# In[8]:


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


# In[9]:


range(10)


# In[10]:


sum(range(4))


# ***
# # 4.4 Break and Continue Statement, else Clauses Loops
# ***

# In[11]:


# Break statement
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # Loop fell through withput findong a factor
        print(n, 'is a prime number')


# In[12]:


# Continue statement
for num in range(2,10):
  if num % 2 == 0:
    print("Found an even number", num)
    continue
  print("Found an odd number", num)


# ***
# # 4.5 Pass Statement
# ***

# In[13]:


# Pass Statement
while True:
  pass # Busy - wait for keyboard interrupt (ctrl + c)


# In[ ]:


class MyEmptyClass:
  pass


# In[ ]:


def initlog(*args):
  pass # Remember to implement this!


# ***
# # 4.6 Match Statement
# ***

# In[44]:


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not allowed"
        case __:
            return "Something's wrong with the internet"


# In[45]:


# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")


# In[110]:


class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
                        


# In[111]:


Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)


# In[112]:


match point:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")


# In[113]:


match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")


# In[54]:


from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")


# ***
# # 4.7 Definig Functions
# ***

# In[56]:


def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    print()


# In[57]:


fib(2000)


# In[58]:


fib


# In[59]:


f = fib


# In[60]:


f(100)


# In[61]:


fib(0)


# In[62]:


print(fib(0))


# In[64]:


def fib2(n): ## Return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0,1
    while a < n:
        result.append(a) # See below
        a,b = b, a+b
    return result


# In[65]:


f100 = fib2(100) # call it


# In[66]:


f100 # Write the result


# ***
# ### 4.8.1 Default Argument Values
# ***

# In[67]:


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


# In[68]:


i = 5

def f(arg=i):
    print(arg)

i = 6
f()


# In[69]:


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# In[70]:


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# ***
# ### 4.8.2 Keyword Arguments
# ***

# In[71]:


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# In[72]:


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# In[75]:


def function(a):
    pass


# In[76]:


function(0, a=0)


# In[77]:


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# In[78]:


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# ***
# ### 4.8.3 Special parameters
# ***

# In[79]:


def standard_arg(arg):
    print(arg)


# In[80]:


def pos_only_arg(arg, /):
    print(arg)


# In[81]:


def kwd_only_arg(*, arg):
    print(arg)


# In[82]:


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# In[83]:


pos_only_arg(1)


# In[84]:


pos_only_arg(arg=1)


# In[85]:


kwd_only_arg(3)


# In[86]:


kwd_only_arg(arg=3)


# In[87]:


combined_example(1, 2, 3)


# In[88]:


combined_example(1, 2, kwd_only=3)


# In[89]:


combined_example(1, standard=2, kwd_only=3)


# In[90]:


combined_example(pos_only=1, standard=2, kwd_only=3)


# In[91]:


def foo(name, **kwds):
    return 'name' in kwds


# In[92]:


foo(1, **{'name': 2})


# In[93]:


def foo(name, /, **kwds):
    return 'name' in kwds


# In[94]:


foo(1, **{'name': 2})


# ***
# ### 4.8.4 Arbitrary Argument Lists
# ***

# In[96]:


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# In[97]:


def concat(*args, sep="/"):
    return sep.join(args)


# In[98]:


concat("earth", "mars", "venus")


# In[99]:


concat("earth", "mars", "venus", sep=".")


# ***
# ### 4.8.5 Unpacking Argument Lists
# ***

# In[100]:


list(range(3, 6))


# In[101]:


args = [3, 6]
list(range(*args))


# In[102]:


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


# In[103]:


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# ***
# ### 4.8.6. Lambda Expressions
# ***

# In[104]:


def make_incrementor(n):
    return lambda x: x + n


# In[105]:


f = make_incrementor(42)
f(0)


# In[106]:


f(1)


# In[107]:


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs


# ***
# ### 4.8.7. Documentation Strings
# ***

# In[108]:


def my_function():
    """Do nothing, but document it.
    
    No, really, it doesn't do anything.
    """
    pass
print(my_function.__doc__)


# ***
# ### 4.8.8. Function Annotations
# ***

# In[109]:


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')


# In[ ]:




