pattern = input()
genome = input()
count = 0
i = 0
while(i < len(genome)-len(pattern)):
    finded = genome.find(pattern, i)
    if finded != -1:
        count += 1
        i = finded + 1
    else:
        i += 1
print(count)