def dna_count(dna):
    dna = dna.upper()
    count_A = dna.count('A')
    count_C = dna.count('C')
    count_G = dna.count('G')
    count_T = dna.count('T')
    return count_A,count_C,count_G,count_T
