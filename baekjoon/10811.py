N, M = map(int,input().split())
basket=[i for i in range(1, N+1)]
    
for _ in range(M):
    i,j=map(int,input().split())
    r= j-i+1
    for _ in range(r//2):
        temp=basket[i-1]
        basket[i-1]=basket[j-1]
        basket[j-1]=temp
        i+=1
        j-=1
    
for i in basket:
    print(i, end=' ')