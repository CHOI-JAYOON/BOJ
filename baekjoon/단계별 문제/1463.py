N=int(input())
def solve(N):
    count=0
    while N>0:
        if N%3==0:
            # N=N//3
            count+=1
            return solve(N//3)
        elif N%2==0:
            # N=N//2
            count+=1
            return solve(N//2)
        else: count+=1
    print(count)

solve(N)
# print(result)

    