import sys
input=sys.stdin.readline

N, M=map(int, input().split())

dict={}

for i in range(1,N+1):
    a=input().rstrip()
    dict[i]=a
    dict[a]=i
    
for i in range(M):
    quest=input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])
    