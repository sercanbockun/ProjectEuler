primenumbers= []
for x in range(2,10000000):
    for a in range(2,int(x**(0.5))+1):
        if x%a ==0:

            break
    else:
        primenumbers.append(x),

bölensayilari=[]

for each in range(10,10000000):
    bölensayisi=0
    for every in primenumbers:
        if each%every ==0:
            bölensayisi+=1
    bölensayilari.append(bölensayisi)

for each in bölensayilari:
    sira = each.index()

    if each ==4 and bölensayilari[sira+1]==4 and bölensayilari[sira+2]==4 and bölensayilari[sira+3]==4:
        print(each)
