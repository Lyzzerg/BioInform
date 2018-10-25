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
complement = {'A':'U', 'C':'G', 'G':'C', 'U':'A'}

dna = list(input())
dnalen = len(dna)
peptide = list(input())
peplen = len(peptide)

for i in range(len(dna)):
    if dna[i] == 'T':
        dna[i] = 'U'
subpep = []
subpepcompl = []
for i in range(dnalen-peplen*3+1):
    substr = []
    substrcompl = []
    for j in range(peplen*3):
        substr.append(dna[i+j])
        substrcompl.append(complement[dna[i+j]])
    subpep.append("".join(substr))
    subpepcompl.append("".join(substrcompl[::-1]))
res = []
for i in range(len(subpep)):
    amin1 = []
    amin2 = []
    for j in range(peplen):
        amin1.append(aminos[subpep[i][j*3:j*3+3]])
        amin2.append(aminos[subpepcompl[i][j*3:j*3+3]])
    if "".join(amin1) == "".join(peptide) or "".join(amin2) == "".join(peptide):
        res.append(list(subpep[i]))
for el in res:
    for i in range(len(el)):
        if el[i] == 'U':
            el[i] = 'T'
for i in range(len(res)):
    print("".join(res[i]))