def ultimator(num):
    sayi=str(num**1000)
    digittoplam=0
    for each in range(len(sayi)):
        digittoplam=digittoplam+ int(sayi[each])
    return digittoplam

print(ultimator(2))

   
        
