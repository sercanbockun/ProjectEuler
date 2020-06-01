def ultimator(num):
    toplam=0
    for each in range(1,num+1):
        toplam += each**each

    toplam2 = str(toplam)


    return toplam2[-10:]


print(ultimator(1000))
        
