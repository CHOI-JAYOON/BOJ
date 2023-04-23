T=int(input())
for _ in range(T):
    A, B = map(int, input().split())
    maxx=0
    
    for i in range(1,A+1):
        if (A%i==0 and B%i==0):
            maxx=i    
    print(maxx*(A//maxx)*(B//maxx))
    