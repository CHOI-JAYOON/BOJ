a=input()
arr=[]
lenga=len(a)
for i in range(1,len(a)+1):
    a=int(a)
    arr.append(int(a%10))
    a=(a-a%10)/10
arr.sort()
# arr.sort(reverse=True)
result=0
for i in range(lenga):
    result+=arr[i]*(10**i)
print(result)


# 정답
# n = int(input())
 
# li = []
# for i in str(n):
#     li.append(int(i))
# # li = list(map(int,str(n))) 으로 변경가능
    
# li.sort(reverse=True) # 내림차순
 
# for i in li:
#     print(i,end='')