T=int(input())

#에라토스테네스 체
arr=[True for _ in range(1000001)]
for i in range(2, 1001):
    if arr[i]:
        for j in range(i+i, 1000001, i):
            arr[j]=False
            
            
for _ in range(T):
    result=0
    N=int(input())
    
    for i in range(2, N//2+1):
        if arr[i] and arr[N-i]:
            result +=1
    print(result)
    
