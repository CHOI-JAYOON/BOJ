A, B = map(int,input().split())
if A>B:
    m=A
else:
    m=B
result=0
max=1
for i in range(1,m+1):
    if(A%i==0 and B%i==0):
        if max<i:
            max=i

print(max*(A//max)*(B//max))   
        
