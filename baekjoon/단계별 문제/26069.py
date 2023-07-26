N=int(input())
dance={'ChongChong'}
for i in range(N):
    A,B=map(str,input().split())
    if A in dance:
        dance.add(B)
    if B in dance:
        dance.add(A)
print(len(dance))
    