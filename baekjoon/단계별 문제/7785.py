import sys
input=sys.stdin.readline

n=int(input())

pe = {}
for _ in range(n):
    name, state=map(str,input().split())
    if(state=="enter"):
        pe[name]='enter'
    else:
        del pe[name]

temp=sorted(pe.keys(), reverse=True)

for i in temp:
    print(i)