N = int(input()) 
account = list(map(int, input().split())) 
M = int(input())
answer = 0

account = sorted(account)
def solution(account, M):
    low, high = 0, max(account)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        total = sum(min(a, mid) for a in account)

        if total <= M:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result
print(solution(account,M))