genome = input()
genomelen = len(genome)
k = int(input())

patterns = []
for i in range(0, len(genome) - k):
    if not (genome[i:i+k] in patterns):
        patterns.append(genome[i:i+k])
patterncount = dict.fromkeys(patterns, 0)

for pattern in patterncount:
    count = 0
    i = 0
    while(i < genomelen - k):
        finded = genome.find(pattern, i)
        if finded != -1:
            count += 1
            i = finded + 1
        else:
            i += 1
    patterncount[pattern] = count
max = 0
for pattern in patterncount:
    if patterncount[pattern] > max:
        max = patterncount[pattern]
for pattern in patterncount:
    if patterncount[pattern] == max:
        print(pattern)