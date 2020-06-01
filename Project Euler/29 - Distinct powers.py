sequence=[]
for each in range(2,101):
    for every in range(2,101):
        if each**every not in sequence:
            sequence.append(each**every)
sequence.sort()
print(sequence)
print(len(sequence))
print(3**5)
