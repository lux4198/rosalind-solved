#!/usr/bin/env python
# coding: utf-8

# In[57]:


from urllib.request import urlopen
from re import finditer

### create list of protein IDs from Input ### 

ID_input = input(str).split()

### create dictionary that stores ID:sequence ### 
sequencedict = {} 

### loop through IDs and find sequences with url "http://www.uniprot.org/uniprot/uniprot_id.fasta" ### 
for item in range(len(ID_input)): 
    url = 'http://www.uniprot.org/uniprot/' + ID_input[item] + '.fasta'
    
    ### print error message if provided ID is invalid ### 
    try: 
        file = urlopen(url).read().decode('utf8')
        file = ''.join(file.splitlines()[1:])
    except: 
        print('Provided ID "' + ID_input[item] + '" is invalid.')
        continue 
        
    sequencedict[ID_input[item]] = file


# In[60]:


### finding motif in example Data ###

### Create motif variable usable in finditer()### 

motif = r'(?=N[^P][ST][^P])'

### define dictionary for output ### 

outputdict = {}

### loop through input list ###

for item in range(len(ID_input)):
    ### check sequence for iterations of motif ### 
    locs = [g.start() + 1 for g in finditer(motif, sequencedict[ID_input[item]])]
    outputdict[ID_input[item]] = locs

# -> print output

for item in outputdict:
    
    if bool(outputdict[item]) != False: 
        print(item, str(outputdict[item]).replace('[', '').replace(',','').replace(']', ''), sep = '\n')

