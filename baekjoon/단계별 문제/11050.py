N,K=map(int,input().split())
n=1
k=1
for i in range(N,N-K,-1):
    n*=i
for j in range(K,0,-1):
    k*=j
print(int(n/k))