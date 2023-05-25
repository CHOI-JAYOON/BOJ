T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    n=1
    m=1
    for i in range(M,M-N,-1):
        m*=i
    for j in range(N,0,-1):
        n*=j
    print(int(m//n))