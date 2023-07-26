import sys
input=sys.stdin.readline
N=int(input())
stack=[]
for i in range(N):
    od=input().strip()

    if od[:4]=="push":
        stack.append(od[5:])
    
    elif od=="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif od=="size":
        print(len(stack))
    elif od=="empty":
        if len(stack)==0:
            print(1)
        else: print(0)
    elif od=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()