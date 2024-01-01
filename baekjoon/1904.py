#01타일
import sys
input=sys.stdin.readline
n=int(input())

arr=[0]*1000001
arr[1]=1
arr[2]=2
arr[3]=3
arr[4]=5

def sol(n):
    for i in range(5,n+1):
        arr[i]=(arr[i-1]+arr[i-2])%15746
        
    print(arr[n])
    
if n==1:
    print(1)
elif n==2:
    print(2)
elif n==3:
    print(3)
elif n==4:
    print(5)
else:
    sol(n)
