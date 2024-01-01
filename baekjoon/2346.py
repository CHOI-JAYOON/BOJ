from collections import deque

N=int(input())

number=list(map(int,input().split()))

bal=deque()
for i in range(1,N+1):
    bal.append(i)
    
start=0
answer=[]

while bal:
    a=bal.popleft()
    answer.append(a)
    start+=number[a-1]

    if start>0:
        bal.rotate(-(start-1))
    else:
        bal.rotate(-start)

for a in answer:
    print(a,end=" ")

# 처음에 스택 사용하려고 했는데 1시간 넘게 안되길래 사용 알고리즘 보니까 덱이였다..
# https://allkong.tistory.com/40#google_vignette 여기서 보면 반례가 같은 넘버를 가진 풍선이 있을 경우라는데 무슨뜻일까요..
# 정답코드
# from collections import deque

# N=int(input())
# bal=deque(enumerate(map(int,input().split())))

# for i in range(N):
#     idx, tmp=bal.popleft()
#     print(idx+1, end=' ')
#     if tmp>0:
#         bal.rotate(-(tmp-1))
#     else:bal.rotate(-tmp)