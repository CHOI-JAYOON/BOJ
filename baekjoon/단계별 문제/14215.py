a, b, c = list(map(int, input().split()))

arr=[]
arr.extend([a,b,c])

maxx=max(arr)
arr.remove(maxx)

if(maxx<arr[0]+arr[1]):
    print(arr[0]+arr[1]+maxx)
else:
    maxx = arr[0]+arr[1]-1
    print(maxx+arr[0]+arr[1])