import bisect

N, M = map(int, input().split())
s=[]
check=[]
for i in range(N):
    s.append(input().strip())
for _ in range(M):
    check.append(input().strip())
    
s.sort()
sum=0
for i in check:
    r=bisect.bisect_right(s,i)
    l=bisect.bisect_left(s,i)
    sum+=(r-l)
    
print(sum)