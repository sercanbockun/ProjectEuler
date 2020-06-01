target = 100
n= target-1
remaining = target-n

while remaining<= n:
    print(n,remaining)
    first_targeters = []
    first_targeters.append(n)
    first_targeters.append(remaining)
    print(first_targeters)

    n -=1
    remaining = target-n


