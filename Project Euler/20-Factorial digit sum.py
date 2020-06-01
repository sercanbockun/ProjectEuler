def fac_num(num):
    factor=1
    toplam=0
    
    for each in range(1,num+1):
        factor = factor*each
    factor1=str(factor)

    for each in factor1:
        
        toplam += int(each)


    return toplam

print(fac_num(100))
        

    
