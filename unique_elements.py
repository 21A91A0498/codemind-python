n=int(input())
m=list(map(int,input().split()))
k=[]
for i in m:
    if i not in k:
        k.append(i)
print(*k)