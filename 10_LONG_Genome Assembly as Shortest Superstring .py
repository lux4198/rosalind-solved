#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format
#       (which represent reads deriving from the same strand of a single linear chromosome).

# The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads
# by gluing together pairs of reads that overlap by more than half their length.

# Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).


import difflib


def get_overlap(s1, s2):
    s = difflib.SequenceMatcher(None, s1, s2, False)
    pos_a, pos_b, size = s.find_longest_match(0, len(s1), 0, len(s2))
    if size >= (len(s2)/2) and (pos_a == 0 or pos_b == 0):
        return (pos_a, pos_b, s1[pos_a:pos_a + size])

def main():
    
    ### Input ### 
    
#     file = open('rosalind.txt', 'r')
    string_list = file.read().split('>')[1:]
    file.close()

    string_list = [''.join(x.split('\n')[1:]) for x in string_list]

    superstring = string_list[0]
    del(string_list[0])

    while string_list:

        for index in range(len(string_list)):

            superstring_end = superstring[-(int((len(string_list[index])/2) + 10)):]
            superstring_beginning = superstring[:int(((len(string_list[index])/2) + 10))]

            if get_overlap(superstring_end, string_list[index]) or get_overlap(superstring_beginning, string_list[index]):
               
                ov = get_overlap(superstring, string_list[index])
                pos_a = ov[0]
                pos_b = ov[1]
                overlap = ov[2]

                if pos_a > pos_b:
                    superstring = superstring.replace(overlap, '')
                    superstring += string_list[index] 
                else:
                    superstring = superstring.replace(overlap, '')
                    superstring = (string_list[index] + superstring)

                del(string_list[index])
                break

#     f = open("output.txt","w+")
    f.write(superstring)
    f.close()  

    print('Done')
    
if __name__ == '__main__':
    main()

