liste=["1","1","2"]
def sira(num,listem):
    for each in range(0,len(listem)):
        if listem[each]==num:
            return each+1
for a in range(0,10000):
    liste.append(str(int(liste[-1])+int(liste[-2])))



for each in liste:
    if 1000<=len(each):
        print(each, "Aradigin sayi:  ",sira(each,liste))
        break




