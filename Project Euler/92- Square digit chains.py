"""Any chain that arrives 1 or 89 stuck in a endless loop. How many numbers below 10000000 will arrive at 89
?
"""
def processor(num):
    chain=[num]
    number=0
    for each in str(num):
        number+= (int(each))**2
    chain.append(number)
    while True:
        zero=0
        for each in str(number):
            
            zero += (int(each))**2
        number=zero
        chain.append(number)
        if number ==1:
            return chain
        elif number==89:
            return chain



    
ten_million= list(reversed(range(1,10000000)))
chain_that_achieved_89 = []
for each in ten_million:
  
    if processor(each)[-1] == 89:
        chain_that_achieved_89.append(processor(each)[0])
"""        for every in processor(each):
            if every in ten_million:
                ten_million.remove(every)       
"""
starters=[89]
print(len(chain_that_achieved_89 ))
print(chain_that_achieved_89 )
"""
for each in chain_that_achieved_89:
    starters.append(each[0])
starters.sort()
print(len(starters))
print(starters)
"""
"""
total_num=0
for each in chain_that_achieved_89:
    for every in each:
        total_num+=1
        
print(total_num)"""

"""for each in reversed(range(1,10000001)):
    number=0
    for x in str(each):
        number += int(each)**2



"""
