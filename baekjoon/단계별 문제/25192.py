N=int(input())
arr=set()
cnt=0
for i in range(N):
    name=input()
    
    if name == "ENTER":
        if arr:
            cnt+=len(arr)
            arr=set()
    else:
        arr.add(name)
if arr:
    cnt+=len(arr)     
print(cnt)


#다시다시닷디사디시디ㅣ
        
