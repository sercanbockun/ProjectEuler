target = 200
n_200 = 200
n_100 = 100
n_50 = 50
n_20= 20
n_10 = 10
n_5 = 5
n_2 = 2
n_1 = 1
count=0

for v_1 in range(0,3):
    for v_2 in range(1+ int((200-v_1*100)/50)):
        for v_3 in range(1 + int((200-v_1*100- v_2*50)/20)):
            for v_4 in range(1 + int((200-v_1*100- v_2*50- v_3*20)/10)):
                for v_5 in range(1 + int((200-v_1*100- v_2*50- v_3*20- v_4*10)/5)):
                    for v_6 in range(1 + int((200-v_1*100- v_2*50- v_3*20- v_4*10- v_5*5)/2)):
                        count += 1
                        
print(count+1)
            
