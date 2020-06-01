liste=[0,1,1]
def fibo(n):
    for a in range(0,n-3):
        liste.append(liste[-1]+liste[-2])

    if liste[-1] < 4000000:
        return liste
    
fibolist = fibo(34)


evenfibo=[]
for x in fibolist:
    if x%2==0:
        evenfibo.append(x)

evenfibotoplam = 0
for y in evenfibo:
    ecenfibotoplam = evenfibotoplam+ y
    


        
         




print(fibolist)
print(evenfibo)
print(sum(evenfibo))
    
