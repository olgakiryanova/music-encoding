from os import write
import random
import re
from itertools import permutations, product
from typing import Dict
import numpy as np

GOMO_REGEX = re.compile(r'(A{2,})|(C{2,})|(T{2,})|(G{2,})', re.IGNORECASE)

def GC(sequence):
    GC_col = sequence.count('G') + sequence.count('C')
    GC_perc = GC_col / len(sequence) * 100
    return GC_perc

def generator(user_data: Dict[str, str]) -> None:
    """Sequence generator function

    Args:
        user_data (Dict[str, str]): General user data for the generator
    Returns:
        str: Returns the path of output file
    """
    nuc = 'ACGT'
    generator_type = user_data['generator_type']
    seq_len = user_data['seq_length']
    seq_num = user_data['num_seqs']
    gc_min, gc_max = user_data['gc_min'], user_data['gc_max']
    NN_min, NN_max = user_data['di_min'], user_data['di_max']
    user_id = user_data['user_id']
    rep_list = set()
    for i in permutations(nuc, 2):
        rep_2 = ''.join(i) * 5
        rep_list.append(rep_2)
    for i in permutations(nuc, 3):
        rep_3 = ''.join(i) * 5
        rep_list.append(rep_3)
    for i in permutations(nuc, 4):
        rep_4 = ''.join(i) * 5
        rep_list.append(rep_4)
    rr = []
    for i in product(nuc, repeat=5):
        rep_5 = ''.join(i)
        if len(GOMO_REGEX.findall(rep_5)) == 0:
            rr.append(rep_5 * 5)
    rep_list.update(rr)
    output_file_name = f'{user_id}_output.csv'
    NN_count = 0
    with open(output_file_name, 'w') as f:
        f.write('sequence                        GC[%]     NN[%]     A[%]    T[%]    С[%]    G[%]\n')
        col_seq = 0
        sequences = set()
        while col_seq < seq_num:

            line = [random.choice(nuc) for i in range(seq_len)]
            if (NN_min == 0) and (NN_max == 0):
                NN_perc = 0
                for i in range(seq_len-1):
                    if line[i] == line[i+1]:
                        line[i+1] = random.choice(list(nuc.replace(line[i], '')))
            else:
                for i in range(seq_len-1):
                    if line[i] == line[i+1]:
                        NN_count = NN_count +1
                NN_perc = NN_count * 2 / seq_len * 100
                if (NN_perc >= NN_min) and (NN_perc <= NN_max):
                   GC_p = GC(line)
            GC_p = GC(line)
            if (GC_p >= gc_min) and (GC_p <= gc_max) and (line not in rep_list) and (line not in sequences):
                sequences.add(line)
                col_seq += 1
            for seq in sequences:
                A_perc = (line.count('A')) / seq_len * 100
                T_perc = (line.count('T')) / seq_len * 100
                G_perc = (line.count('G')) / seq_len * 100
                C_perc = (line.count('C')) / seq_len * 100
                f.write(f'{seq}; {np.round(GC_p, 2)};{np.round(NN_perc, 2)};{np.round(A_perc, 2)};{np.round(T_perc, 2)};{np.round(C_perc, 2)};{np.round(G_perc, 2)}\n')
    answer = input()
