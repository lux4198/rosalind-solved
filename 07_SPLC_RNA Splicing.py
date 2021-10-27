#!/usr/bin/env python
# coding: utf-8

# In[71]:


# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. 
# All strings are given in FASTA format.

# Return: A protein string resulting from transcribing and translating the exons of s.
# (Note: Only one solution will exist for the dataset provided.)

import re


def check_ORF(start_codons, stop_codons):
    ORF_positions = []
    # loop through positions of start codon 
    for start in start_codons: 
    # compare start codon position to stop codon position 
        for stop in stop_codons:
            # ORF has to be divisible by 3 
            if start < stop and ((stop-start)%3) == 0:
                    # create tuple with ORF position and append to list 
                    ORF_positions.append((start,stop))
                    return ORF_positions
            else:
                continue
    # return list of ORF positions 
    return ORF_positions 


def create_triplets(string, ORF_positions):
    # split ORF in triplets and append them to list 
    triplets_list = [[string[index:index+3] for index in range(item[0], item[1], 3)] for item in ORF_positions]
    return triplets_list


def translate_triplets(triplets_list, DNA_codons):
    # translate triplets into protein sequence and store sequences in a list
    sequences = [''.join([DNA_codons[triplet] for triplet in item]) for item in triplets_list]
    return sequences


DNA_codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}


input_file = open('rosalind_splc.txt', 'r')
input_file = input_file.read().split('>')

sequence = ''.join(input_file[1].split('\n')[1:])

introns = [''.join(x.split('\n')[1:]) for x in input_file[2:]]

n = 0
for intron in introns:
    sequence = sequence.replace(intron, '')

# find positions of start codons in string
locs_start = [g.start() for g in re.finditer(r'ATG', sequence)]

# find positions of stop codons in string 
stop_codons = r'TAA|TGA|TAG'
locs_stop = [g.start() for g in re.finditer(stop_codons, sequence)]

ORF_positions = check_ORF(locs_start, locs_stop)

# create triplets
triplets_list = create_triplets(sequence, ORF_positions)

# translate triplets into protein strings 
prot_strings = translate_triplets(triplets_list, DNA_codons)

print(str(prot_strings[0]))

