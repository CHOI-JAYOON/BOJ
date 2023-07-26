import sys
input=sys.stdin.readline
T=int(input())
for tc in range(T):
    stack=[]
    ps=input().strip()
    for j in range(len(ps)):
        if ps[j]=='(':
            stack.append('(')
        elif ps[j]==')':
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(')')
                
    if len(stack)==0 :
        print("YES")
    else:
        print("NO")