import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    answer=[]
    data=input().strip()
    for d in data:
        if d=='(':
            answer.append('(')
        else:
            if len(answer)==0 or answer[-1]==')':
                answer.append(')')
            else: 
                answer.remove('(')
    if len(answer)==0:
        print("YES")
    else: print("NO")
    
    