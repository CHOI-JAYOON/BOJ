K=int(input())

data=[]

for _ in range(K):
    num=int(input().strip())
    if num!=0:
        data.append(num)
    else: data.pop()
       

print(sum(data))
