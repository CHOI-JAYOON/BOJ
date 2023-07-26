number=[]

for i in range(1,10001):
    number.append(i)


for i in range(1,10001):
    if i<10:
        result=i+i//1
        if result in number:          
            number.remove(result)
        else: continue
        
    elif i<100:
        result=i//10+i%10+i
        if result in number:
            number.remove(i//10+i%10+i)
        else: continue
        
    elif i<1000:
        result=i//100+(i%100)//10+i%10+i
        if result in number:
            number.remove(result)
        else: continue
        
    elif i<=10000:
        result=(i//1000)+((i%1000)//100)+((i%100)//10)+(i%10)+i
        if result in number:
            number.remove(result)
        else:continue
            
for num in number:
    print(num)