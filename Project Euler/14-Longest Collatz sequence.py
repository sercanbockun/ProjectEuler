def birleme(number):
    islemsayisi=0
    while number> 1:
        if number%2==0:
            number=number/2
            islemsayisi+=1
        elif number%2==1:
            number=number*3 + 1
            islemsayisi+=1
    return islemsayisi


biggestlength=0
basariliolanlar=[]
for x in range(2,1000000):
    if birleme(x)> biggestlength:
        biggestlength=birleme(x)
        basariliolanlar.append(x)



print(biggestlength)
print(basariliolanlar[-1])
    
   
