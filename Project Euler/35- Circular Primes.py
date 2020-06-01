
primenumbers= []
for x in range(2,1000000):
    for a in range(2,int(x**(0.5))+1):
        if x%a ==0:
            break
    else:
        primenumbers.append(x)


def isPrime(num):
    for a in range(2,int(num**(0.5)+1)):       
        if x%a ==0:
            return False
    else:
        return True

def comb(each):
    for num in str(each):
        if num in '024568':
            return False
        else:
            continue
    circ_nums = []
    for i in range(1, len(str(each))):
        each = str(each)
        new_num = each[i:len(each)] + each[0:i]
        if isPrime(int(new_num)) == False:
            return False
        else:
            continue
    return True
count= 0
for every in primenumbers:
    if comb(every) == True:
        count+=1
    else:
        continue
print(count)
        
