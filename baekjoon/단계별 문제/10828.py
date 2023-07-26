import sys
input=sys.stdin.readline
N=int(input())
arr=[]
for _ in range(N):
    A=sys.stdin.readline().split()
    if A[0]=='push':
        # a,b=A.split()
        arr.append(A[1])
    elif A[0]=='pop':
        if len(arr)==0:
            print(-1)
        else:
            print(arr[-1])  
            arr.pop()
    elif A[0]=='top': 
        if len(arr)==0:
            print(-1)
        else:
            print(arr[-1])       
    elif A[0]=='empty':
        if len(arr)==0:
            print(1)
        else:
            print(0)
    elif A[0]=='size':
        print(len(arr))

    
        
        