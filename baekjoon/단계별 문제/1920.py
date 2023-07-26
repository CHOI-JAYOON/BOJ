import sys
input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))
M=int(input())
arr2=list(map(int,input().split()))

arr=set(arr)

for i in arr2:
    if i in arr:
        print(1)
    else:print(0)
