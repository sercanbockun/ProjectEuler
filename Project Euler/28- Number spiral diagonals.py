sayi = 1
toplam=1
for nums in range(2,1001,2):
    toplam+=  (sayi+ float(nums)*1) + (sayi+float(nums)*2)+ (sayi+float(nums)*3)+ (sayi+float(nums)*4)
    sayi = sayi+ 4*nums


print(toplam)
    
