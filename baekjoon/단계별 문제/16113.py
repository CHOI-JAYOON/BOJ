N=int(input())
s=input()
# length=int(len(s))
# c=int(length/5)
board=[[0]*int(N/5) for i in range(5)]
c=0
for i in range(5):
    for j in range(int(N/5)):
        if s[j+(i*int(N/5))]=='#':
            board[i][j]=1
        else:
            board[i][j]=0
    # j+=(int(N/5))
    
# for i in range(int(N/5)):
#     for j in range(5):
#         if s=='#':
#             board[i][j].append(1)
#         else:
#             board[i][j].append(0)

for i in range(5):
    for j in range(int(N/5)):
        print(board[i][j],end="")
    print()