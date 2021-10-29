#!/usr/bin/env python
# coding: utf-8

# In[34]:


# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

# Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.
# (use the standard order of symbols in the English alphabet).

import itertools 


def main():
    # input characters as string and remove spaces 
    characters = 'A B C D E F G H' 
    characters = characters.replace(' ', '')
    n = 3

    # print out product generator 
    for a, b, c  in itertools.product(characters, repeat=n):
        print(a + b + c)
        
if __name__ == '__main__':
    main()

