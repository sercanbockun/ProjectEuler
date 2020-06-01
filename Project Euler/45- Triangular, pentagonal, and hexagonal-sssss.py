def triangle(x):
    sayi = x*(x+1)/2
    return sayi
def pentagon(y):
    sayi=y*(3*y-1)/2
    return sayi
def hexagon(z):
    sayi = z*(2*z-1)
    return sayi
tri= []
penta=[]
hexa=[]
basariliolanlar=  []


for each in range(1,50000):
    
    
    a=triangle(each)
    b=pentagon(each)
    c=hexagon(each)
    tri.append(a)
    penta.append(b)
    hexa.append(c)
    
for each in tri:
    for x in penta[:tri.index(each)+1]:
        if each==x:
            for y in hexa[:tri.index(each)+1]:
                if y ==each:
                    basariliolanlar.append(each)

print(basariliolanlar)
print(basariliolanlar[-1])


    

