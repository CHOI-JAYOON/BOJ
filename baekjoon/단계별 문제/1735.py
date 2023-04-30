A, B = map(int,input().split())
C, D = map(int,input().split())

E=(A*D)+(B*C)
F=(B*D)
max=1
for i in range(1,F+1):
    if(E%i==0 and F%i==0):
        max=i
    
print(E//max, F//max)
