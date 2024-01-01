#도키도키 간식드리미
from collections import deque
N=int(input())
number=deque(map(int,input().split())) #FIFO

temp=[] # LIFO
snack=1
result=0
while number:
    num=number.popleft()
    if snack!=num:
        temp.append(num)
        # print("temp",temp)
    else:
        snack+=1
        # print("snack",snack)
        
    while temp:
        tmp=temp[-1]
        if snack==tmp:
            temp.pop()
            snack+=1
            # print("snack",snack)
        else:
            break
        
    
if len(temp)==0 and len(number)==0:
    result=0
else: result=1
    
if result==1:
    print("Sad")   
else: print("Nice")