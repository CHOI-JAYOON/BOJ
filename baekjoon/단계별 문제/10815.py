import sys
import bisect
input=sys.stdin.readline
a=[]
b=[]

N=int(input())
a=list(map(int,input().split()))
M=int(input())
b=list(map(int,input().split()))

a.sort()

for i in b:
    r=bisect.bisect_right(a,i) # 정렬된 리스트에서 target의 위치+1
    l=bisect.bisect_left(a,i) #정렬된 리스트에서 target의 위치
    print(r-l, end=' ') # 정렬된 리스트에서 특정 값이 몇번 등장하는지 확인
    