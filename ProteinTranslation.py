aminos = {'AAA':'K', 'AAC':'N', 'AAU':'N', 'AAG':'K',
          'ACA':'T', 'ACC':'T', 'ACU':'T', 'ACG':'T',
          'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
          'AGA':'R', 'AGC':'S', 'AGU':'S', 'AGG':'R',
          'CAA':'Q', 'CAC':'H', 'CAU':'H', 'CAG':'Q',
          'CCA':'P', 'CCC':'P', 'CCU':'P', 'CCG':'P',
          'CUA':'L', 'CUC':'L', 'CUU':'L', 'CUG':'L',
          'CGA':'R', 'CGC':'R', 'CGU':'R', 'CGG':'R',
          'UAA':'*', 'UAC':'Y', 'UAU':'Y', 'UAG':'*',
          'UCA':'S', 'UCC':'S', 'UCU':'S', 'UCG':'S',
          'UUA':'L', 'UUC':'F', 'UUU':'F', 'UUG':'L',
          'UGA':'*', 'UGC':'C', 'UGU':'C', 'UGG':'W',
          'GAA':'E', 'GAC':'D', 'GAU':'D', 'GAG':'E',
          'GCA':'A', 'GCC':'A', 'GCU':'A', 'GCG':'A',
          'GUA':'V', 'GUC':'V', 'GUU':'V', 'GUG':'V',
          'GGA':'G', 'GGC':'G', 'GGU':'G', 'GGG':'G'}
rna = input()
i = 0
rnalen = len(rna)
translation = []
while (i < rnalen - 2):
    codon = aminos[rna[i:i+3]]
    if codon != '*':
        translation.append(codon)
        i += 3
    else:
        break
print("".join(translation))