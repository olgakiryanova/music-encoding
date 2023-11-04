import os 
import time

import numba
import numpy as np
import pandas as pd
from numba import prange

if __name__ == "__main__":

    answer = 'y'
    while answer not in ['no', 'n', 'N']:
        print('Choose type of sequence 1-binary, 2-DNA')
        answer = input()
        print('Input filename')
        name_file = input()
        if answer == '1':
            print('You chosen binary\n')
            with open(name_file, 'r') as f:
                text = f.read()
                idx = 0
                bin_text = ''
                dna_res = ''
                while idx <= len(text):
                    binseq = text[idx : idx + 8]
                    bin_text = bin_text + binseq + ' '
                    dna_seq = binseq.replace('00', 'C')
                    dna_seq = dna_seq.replace('11', 'T')
                    dna_seq = dna_seq.replace('1', 'G')
                    dna_seq = dna_seq.replace('0', 'A')   
                    dna_res = dna_res + dna_seq
                    idx = idx + 8  
                f1 = open('binary.txt', 'w')
                f1.write(bin_text)
                f1.write('\n \n \n')
                f1.write(dna_res)
                f1.close()
            f.close()
            
        if answer == '2':
            result_seq = ''
            print('You chosen DNA\n')
            print('Input filename')
            name_file2 = input() 
            with open(name_file2, 'r') as f3:
                dnaseq = f3.read().upper()
                print('dna')
                bin_seq = dnaseq.replace('C', '00')
                bin_seq = bin_seq.replace('T', '11')
                bin_seq = bin_seq.replace('G', '1')
                bin_seq = bin_seq.replace('A', '0')
                result_seq = result_seq + bin_seq
                idx = 0
                bin_text = ''
                while idx <= len(result_seq):
                    binseq = result_seq[idx : idx + 8]
                    #print (binseq)
                    bin_text = bin_text + binseq + ' '
                    idx = idx + 8 
                print(bin_text)
                f2 = open('nucleotide.txt', 'w')
                f2.write(dnaseq)
                f2.write('\n \n \n')
                f2.write(bin_text)
                f2.close()
            f3.close()
