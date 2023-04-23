N=int(input())
arr=[]
for _ in range(N):
    age, name = list(input().split())
    age=int(age)
    arr.append([age,name])
    
arr.sort(key=lambda x : x[0]) # (age, name)에서 age만 비교

for age, name in arr:
    print(age, name)