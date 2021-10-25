#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Given: A protein string P of length at most 1000 aa.

# Return: The total weight of P.

# read mass table and create dictionary of protein masses 
# loop through list of string and add mass to total mass number 

table = '''A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333'''

masstable_dict = {}
i = 0
while i < len(table.split()) - 1:
    masstable_dict[table.split()[i]] = float(table.split()[i+1])
    i += 2

string_input = list(input(str()))

total_mass = 0
for item in string_input: 
    total_mass += masstable_dict[item]
    
print(round(total_mass, 3))

