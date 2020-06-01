for num in range(1,1000000):
    sayilar=[]
    for each in range(1,7):
        x= str(num*each)
        y = sorted(x)
        sayilar.append(y)
        if 6<= len(sayilar)  and sayilar[0]==sayilar[1]==sayilar[2]==sayilar[3]==sayilar[4]==sayilar[5]:
            print(num)
            break
        else:
            continue
