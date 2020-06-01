target = 2000000

sucessors = []
"""
for n_1 in range(0,2000000):
    for n_2 in range(0,2000000):
        horizontal = n_1
        vertical = n_2
        num_of_rects = ((horizontal)*(horizontal -1)/2) * ((vertical)*(vertical -1)/2)
        diff = 2000000 - num_of_rects
        if diff < current_diff:
            diff = current_diff
            sucessors.append([n_1, n_2])
	   """

n_1 = 2000
n_2 =1
diff = target
while (n_1> n_2):
    num_of_rects = (n_1)*(n_1 -1) * (n_2)*(n_2 -1)/4
    current_diff =  abs(num_of_rects - 2000000)
    if current_diff < diff:
        diff = current_diff
        sucessors.append([n_1, n_2])
        print(diff)
        print(num_of_rects)

    if num_of_rects > target:
        n_1 -=1
    elif num_of_rects< target:
        n_2 += 1
    
print(sucessors)
print(f"The area is {(sucessors[-1][0] -1 )* (sucessors[-1][1]-1)}")
	
    
