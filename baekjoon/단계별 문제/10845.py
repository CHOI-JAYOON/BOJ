import sys
from collections import deque
input=sys.stdin.readline

data=deque()

N=int(input())
for _ in range(N):
    od=input().strip()
    if od[:4]=="push":
        data.append(od[5:])
    elif od=="pop":
        if len(data)==0:
            print(-1)
        else:
            a=data.popleft()
            print(a)
    elif od=="size":
        print(len(data))
    elif od=="empty":
        if len(data)==0:
            print(1)
        else:print(0)
    elif od=="front":
        if len(data)==0:
            print(-1)
        else:print(data[0])
    elif od=="back":
        if len(data)==0:
            print(-1)
        else:print(data[-1])
        
    