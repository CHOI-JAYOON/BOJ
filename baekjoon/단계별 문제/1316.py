import sys
input=sys.stdin.readline

N=int(input())
count=0
for i in range(N):
    answer=''
    word=input().strip()
    answer+=word[0]
    
    for j in range(1,len(word)):
        if word[j]!=word[j-1] and word[j] not in word[:j]:
            answer+=word[j]
            
        elif word[j]==word[j-1]:
            answer+=word[j]
            
        else: answer=''
    if answer == word:
        count+=1
            
print(count)
             
    
