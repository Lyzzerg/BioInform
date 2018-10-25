aminomas = {"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113, "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186}
    

peptide = list(input())
weights = []
for p in peptide:
    weights.append(aminomas[p])
res = []
i=0
j=0
count = 0
for i in range(1, len(peptide)):
    j=0
    count=0
    while count < len(peptide):
        summ = 0
        for k in range(i):
            if j == len(peptide):
                j = 0
            summ += weights[j]
            j += 1
        j -= k
        res.append(summ)
        count += 1
res.append(0)
res.append(sum(weights))
res.sort()
print(" ".join(str(x) for x in res))