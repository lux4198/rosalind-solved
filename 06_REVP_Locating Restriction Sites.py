#!/usr/bin/env python
# coding: utf-8

# In[55]:


# Given: A DNA string of length at most 1 kbp in FASTA format.

# Return: The position and length of every reverse palindrome in the string having length between 4 and 12.
# You may return these pairs in any order.


import time

t0 = time.time()

def check_palindrome(string_input, current_pos, i, j, k):
    # current_pos and i are needed for exit condition 
    # j,k : current_pos and i, however j,k change during function
    position = ()
    # 1. condition, bases are not the same -> return false and try next palindrome length
    if string_input[j] != reverse(string_input, k):
        return False 
    
    # exit condition -> bases at the end of palindrome length are the same
    elif string_input[j] == reverse(string_input, k) and j == current_pos and k == (current_pos + i - 1):
        return True
    
    # 2. condition, bases are the same -> move from center to sides 
    else:
        if k < (current_pos + i) and j > current_pos:
            k += 1
            j -= 1
        return check_palindrome(string_input, current_pos, i, j, k)

# returns complement base of base in original string     
def reverse(string, index):
    rev_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return rev_dict[string[index]]

# input dna sequence in fasta format 
string_input = open('rosalind_revp-1.txt', 'r')
string_input = list(''.join(string_input.read().split('\n')[1:]))

# string_input = 'TCAATGCATGCGGGTCTATATGCAT'

# file = open('output1.txt', 'w+')

length = len(string_input)

# loop through dna sequence
for index in range(length):
    # at every position examine if palindrome of certain length can be found 
    for i in range(4,13,2):
        # j,k variables that are used for comparing positions of string and reverse string
        j = int(index + (i/2) - 1) 
        k = int(index + (i/2)) 
        if index + i > length:
            break
        elif check_palindrome(string_input, index, i, j, k):
#             file.write(str(index + 1) + ' ' + str(i) + '\n')
        else:
            continue

# file.close()

t1 = time.time()

print(t1-t0)

