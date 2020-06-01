liste=[]

for each in range(2,1000000):
    sayi=str(each)
    toplam=0
    for x in sayi:
        toplam += int(x)**5
    if toplam == each:
        liste.append(each)

print(liste)
print(sum(liste))
