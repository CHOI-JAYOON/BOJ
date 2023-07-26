while(1):
    s=input()
    stack=[]
    if s=='.':
        break
    else:
        for j in range(len(s)):
            if s[j]=='(' or s[j]=='[':
                stack.append(s[j])
            elif s[j]==')':
                if len(stack)!=0 and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(')')
                    break
            elif s[j]==']' :
                if len(stack)!=0 and stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(']')
                    break
                    
    if len(stack)==0:
        print("yes")
    else:
        print("no")
    
    