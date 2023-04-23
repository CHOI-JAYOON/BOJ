import sys
input=sys.stdin.readline

N=int(input())
arr=[]
for i in range(N):
    [a, b]=map(int, input().split())
    arr.append([b,a])

s_arr=sorted(arr)

for b, a in s_arr:
    print(a, b)