N,M=map(int,input().split())
basket=[0]*(N+1)
temp=0

for i in range(N+1):
    basket[i]=i
    
for _ in range(M):
    i,j=map(int, input().split())
    temp = basket[i]
    basket[i]=basket[j]
    basket[j]=temp

for i in range(1, N+1):
    print(basket[i], end=' ')