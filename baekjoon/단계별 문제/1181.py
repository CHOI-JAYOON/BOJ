import sys
input=sys.stdin.readline

N=int(input())
lst=[]
for i in range(N):
    lst.append(input().strip())

set_lst=set(lst) #set으로 변환해서 중복값을 제거
lst=list(set_lst)

lst.sort() #괄호 안에 아무 값도 넣지 않으면 알파벳 순서대로 정렬을 해 준다.
lst.sort(key=len)

for i in lst:
    print(i)


