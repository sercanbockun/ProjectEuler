def IsPenta(x):
    if ((24*x+1)**(1/2) + 1 )%6 ==0:
        return True
    return False

def Pentagon(n):
    return n*(3*n-1)/2


i = 1
while True:
    for j in range (1,i):
        summ = Pentagon(i) + Pentagon(j)
        subs = abs(Pentagon(i)- Pentagon(j)) 
        if IsPenta(summ)==True and IsPenta(subs) == True:
            print (subs)
            False
    
    i += 1
    
