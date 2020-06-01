from itertools import permutations

def IsPrime(x):
    for i in range(2,int(x**(1/2)+1)):
        if x%i==0:
            return False
    return True

biggest_num = 0
perms = []
for every in range(1,10):
    perm = permutations([1,2,3,4,5,6,7,8,9],every)
    perm = list(perm)
    for each in perm:
        each = list(each)
        b = [str(x) for x in each]
        c = int(''.join(b))
        if IsPrime(c) == True:
            perms.append(c)

print(perms[-1])
