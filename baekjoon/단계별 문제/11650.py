import sys
input=sys.stdin.readline

N = int(input())

arr=[]

for i in range(N):
    [a,b]=map(int, input().split())
    arr.append([a,b])

s_arr=sorted(arr)

for i in range(N):
    print(s_arr[i][0], s_arr[i][1])

