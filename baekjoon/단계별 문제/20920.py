import sys
input=sys.stdin.readline
N,M=map(int,input().split())
wordArr={}
for i in range(N):
    word=input().strip()
    if len(word)>=M:
       if word in wordArr:
           wordArr[word]+=1
       else:
           wordArr[word]=1
word_dict=sorted(wordArr.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))

for word in word_dict:
    print(word[0])
    

    