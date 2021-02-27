def dna_count(dna): #counts each nucleotide in DNA
    dna = dna.upper()
    count_A = dna.count('A')
    count_C = dna.count('C')
    count_G = dna.count('G')
    count_T = dna.count('T')
    return count_A,count_C,count_G,count_T
def reverse_complement(dna[::-1]): #gives the reverse complement of DNA
    compl = ''
    for symbol in dna[::-1]:
        if symbol == 'A':
            compl = compl + 'T'
        elif symbol == 'T':
            compl = compl + "A"
        elif symbol == 'C':
            compl = compl + "G"
        elif symbol == 'G':
            compl = compl + "C"
    return compl
#RNA2codons
     def rna2codon(triplet):
        genetic_code = {
            'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',

            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',

            'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',

            'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
            'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
        }
        allowed_codons = set('ACGU')
        if triplet in genetic_code:
            x=genetic_code[triplet]
            return x
        else:
            return "Invalid"
    def rna2codons(triplets):
        amino= ''
        for i in range( 0,int( len(triplets) / 3 ) ):
            amino= amino+ rna2codon(triplets[ 3*i:3*i+3])
        return amino
    return rna2codons(triplets)
