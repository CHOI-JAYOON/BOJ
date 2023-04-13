A=[]

for i in range(9):
    i=list(map(int,input().split()))
    A.append(i)

X=0
Y=0
max=-1

for i in range(9):
    for j in range(9):
        if(A[i][j]>max):
            max=A[i][j]
            X=i+1
            Y=j+1
            
print(max)     
print(X, Y)