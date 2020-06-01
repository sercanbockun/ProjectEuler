toplamsayi=0
sayilar=[]
for each in range(1,1000000):
    for x in range(1,7):
        if len(str(each))==x:
            for y in range(0,x):
                sayilar.append(int(str(each)[y]))



print(sayilar[0]*sayilar[9]*sayilar[99]*sayilar[999]*sayilar[9999]*sayilar[99999]*sayilar[999999])
