#!/usr/bin/env python
# coding: utf-8

# In[47]:


### Given: A protein string of length at most 1000 aa.

### Return: The total number of different RNA strings from which 
              # the protein could have been translated, modulo 1,000,000.

# convert input string to list 
sequence = list(input(str))

# store number of possible triplets for each AA in dictionary 

triplet_number = {
    'F': 2, 'L':6, 'S':6, 
    'Y':2, 'C':2, 'W':1, 
    'P':4, 'H':2, 'Q':2, 
    'R':6, 'I':3, 'M':1, 
    'T':4, 'N':2, 'K':2,
    'V':4, 'A':4, 'D':2, 
    'E':2, 'G':4
}


# set variable for possible solutions (3 bc of stop codon)
n = 3

# loop through sequence list 
for item in range(len(sequence)):

    n *= triplet_number[sequence[item]]
        
n %= 1000000
print(n)
#181376

