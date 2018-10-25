complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
dna = list(input())
for i in range(len(dna)):
    dna[i] = complement[dna[i]]
print("".join(dna[::-1]))