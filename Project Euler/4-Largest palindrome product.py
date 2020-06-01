x= range(100,1000)
y=range(100,1000)
liste=[]
enbüyük=[111111]
for a in x:
    for b in y:
        sayi=str(a*b)
        for t in range(0,len(sayi)//2):
            if sayi[t]!=sayi[-t-1]:
                break

        else:
            liste.append(sayi)


for each in liste:
    if int(enbüyük[0])<int(each):
        enbüyük[0]= each

    else:
        continue

print(enbüyük[0])
        
                

           
                
        
            
