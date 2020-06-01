#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and
#4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def factorial(n):
    num=1
    for each in range(1,n+1):
        num = num*each

    return num

surprise=[]
number=1000000
for each in reversed(range(1,10)):    
    for nums in range(1,99999):
        if number<= factorial(each)*nums:
            surprise.append(nums-1)
            number= number-factorial(each)*(nums-1)
            break
            
        else:
            continue

print(surprise)
first_ten_nums=[0,1,2,3,4,5,6,7,8,9]
our_number = ""
for each in surprise:
    our_number= our_number + str(first_ten_nums[each])
    first_ten_nums.remove(first_ten_nums[each])
    
print(f"Millionth lexicographic number is : {our_number}")




        
        
                
        
        
    

