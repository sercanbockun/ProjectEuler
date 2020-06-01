
primenumbers= []
for x in range(2,100000000):
    for a in range(2,int(x**(0.5))+1):
        if x%a ==0:

            break
    else:
        primenumbers.append(x)
        if len(primenumbers)==10001:
            
           
            print(primenumbers[-1])
            break   
print(primenumbers)


    
    



