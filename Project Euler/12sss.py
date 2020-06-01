
primenumbers= []
for x in range(2,1000):
    for a in range(2,x):
        if x%a ==0:

            break
    else:
        primenumbers.append(x)
        
print( primenumbers)
        

def triangle(n):
    sayilar=int(n*(n+1)/2)
    
    return sayilar

def bölensayisi(num):
    sayi=0
    for each in range(1,(num+1)):
        if  num%each==0:
            sayi=sayi+1

    return sayi

for each in range(76576499,76576501):
    for every in primenumbers:
        dividers=[]
        if each%every==0:
            dividers.append(every)
    print(dividers)

  
       
    

    
