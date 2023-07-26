s=input().replace(',','')[:-1].split(' ')
for i in range(1,len(s)):
    s[i]=s[i].replace('[]','][')
for i in range(1,len(s)):
    a=s[0]
    name=''
    length=len(s[i])
    
    for j in range(length-1,-1,-1):
        if s[i][j]=='*'or s[i][j]=='&'or s[i][j]=='[' or s[i][j]==']':
            a=a+s[i][j]
        else:
            name=name+s[i][j]
    name="".join(reversed(name))
    print('{0} {1};'.format(a,name))

