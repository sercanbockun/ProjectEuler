primenumbers= []
for x in range(2,2000000):
    for a in range(2,int(x**(0.5))+1):
        if x%a ==0:

            break
    else:
        primenumbers.append(x)
print(primenumbers)
print(sum(primenumbers))
        
