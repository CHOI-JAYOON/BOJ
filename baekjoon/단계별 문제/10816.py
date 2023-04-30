import sys
input=sys.stdin.readline

N=int(input())
a=map(int,input().split())
M=int(input())
b=map(int,input().split())

hashmap={}
for n in a:
    if n in hashmap:
        hashmap[n]+=1
    else:
        hashmap[n]=1
    
print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in b))