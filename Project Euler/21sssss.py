çiftler=[]
for x in range(2,10000):
    bölenler= []
    for a in range(2,x):
        if x%a ==0:
            
            bölenler.append(x)
    toplam= sum(bölenler)
    for y in range(2,10000):
        bölenler2=[]
        for b in range(2,y):
            if y%b==0:
                bölenler2.append(y)

    toplam2=sum(bölenler2)
    if toplam==toplam2:
        çiftler.append([x,y])

print(çiftler)
            
