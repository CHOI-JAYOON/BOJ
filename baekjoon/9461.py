T=int(input())

def sol(N):
    for i in range(11,N+1):
        d[i]=d[i-1]+d[i-5]
    print(d[i])
        
for t in range(T):
    N=int(input())
    d=[0]*(N+11)
    d[0]=0
    d[1]=1
    d[2]=1
    d[3]=1
    d[4]=2
    d[5]=2
    d[6]=3
    d[7]=4
    d[8]=5
    d[9]=7
    d[10]=9
    if N<=10:
        print(d[N])
    else:
        sol(N)
    