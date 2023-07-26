N,K=map(int,input().split())
arr=[]
result=[]
for i in range(1,N+1):
    arr.append(i)
    
for i in range(1,N+1):
    if len(arr)>K:
        # n=arr[2]
        result.append(arr[K-1])
        arr.remove(arr[K-1])
    else:
        break    
    
result.append(arr)
print(result)

#다시!!
