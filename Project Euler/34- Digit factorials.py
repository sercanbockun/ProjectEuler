def factorial(n):
    num=1
    for each in range(1,n+1):
        num = num*each
    if n==0:
        return 1
    return num

sum_all=0
for each in range(3,999999):
    sum = 0
    for every in range(0,len(str(each))):
        sum += factorial(int(str(each)[every]))

    if sum == each:
        print(each)
        sum_all+= each

print(f"number you are looking for is : {sum_all} ")
