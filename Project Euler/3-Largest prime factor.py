
bölenler=[]
for numbers in range(2,int(600851475143**0.5)):
    
    if 600851475143%numbers!=0:
        continue
    else:
            
        bölenler.append(numbers)


    

print(bölenler)

asallar=[]
for each in bölenler:
    for x in range(3,int(each**0.5)):
        if each%x==0:
            break
    else:
          
        asallar.append(each)

print(asallar)
            
        
    
        
    

