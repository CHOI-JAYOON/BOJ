N=int(input())
arr=list(map(int,input().split()))
arr.sort()
sum=0

for i in range(N):
    for j in range(i+1):
        sum+=arr[j]

print(sum)
#필요한 시간의 합이 최솟값이려면 걸리는 시간이 짧은 사람이 앞으로 오도록
#정렬해서 앞에서부터 더해줌