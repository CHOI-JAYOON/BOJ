import sys
input=sys.stdin.readline

word=input().strip()
count=len(word)

for i in range(len(word)):
    if word[i:i+2]=='c=':
        count-=1
          
    elif word[i:i+2]=='c-':
        count-=1
          
    elif word[i:i+3]=='dz=' :
        count-=1
           
    elif word[i:i+2]=='d-':
        count-=1
           
    elif word[i:i+2]=='lj' :
        count-=1
        
    elif word[i:i+2]=='nj':
        count-=1

       
    elif word[i:i+2]=='s=' :
        count-=1
       
    elif word[i:i+2]=='z=' :
        count-=1
       
    else:
        continue
    
print(count)