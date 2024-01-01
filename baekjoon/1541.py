op=input().split('-')
num=[]

for i in op:
    sum=0
    n=i.split('+')
    for j in n:
        sum+=int(j)
    num.append(sum)
    
first=num[0]

for i in range(1,len(num)):
    first-=num[i]
print(first)
    

