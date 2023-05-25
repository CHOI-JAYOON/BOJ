import sys
#input=sys.stdin.readline
N=int(input())
result=0
x=1
while x*x<=N:
    x+=1
    result+=1
print(result)