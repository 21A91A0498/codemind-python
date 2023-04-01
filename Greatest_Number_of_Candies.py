n=int(input())
arr=list(map(int,input().split()))
m=int(input())
l=[]
for i in range(len(arr)):
    if (arr[i]+m)>=max(arr):
        l.append(True)
    else:
        l.append(False)
print(*l)