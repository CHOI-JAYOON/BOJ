from collections import deque

N=int(input())
arr=deque([])

for i in range(1,N+1):
    arr.append(i)
    
for i in range(len(arr)):
    if len(arr)==1:
        break
    arr.popleft()
    arr.append(arr[0])
    arr.popleft()


print(*arr)
    