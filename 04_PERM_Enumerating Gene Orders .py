#!/usr/bin/env python
# coding: utf-8

# In[29]:


import math 
from itertools import permutations

# Given: A positive integer n≤7
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

n = int(input())
numbers = (x for x in range(1,n + 1))
permutations = [str(x) for x in permutations(numbers)]

print(math.factorial(n))
print(*(x.replace('(', '').replace(',', '').replace(')', '') for x in permutations), sep = '\n')

