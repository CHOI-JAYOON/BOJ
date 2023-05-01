import sys
from math import gcd
input=sys.stdin.readline

N=int(input())
#첫 가로수 위치
a=int(input())
arr=[]
#가로수들 사이의 간격 저장
for _ in range(N-1):
    num=int(input())
    arr.append(num-a)
    a=num
    
#arr에 들어있는 모든 수들의 최대공약수 찾기
g=arr[0]
for j in range(1,len(arr)):
    g=gcd(g,arr[j])
    
# 둘 사이에 심을 가로수 개수 : 간격//최대공약수 -1
result=0
for each in arr:
    result+=each//g-1

print(result)