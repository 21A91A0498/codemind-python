n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
c=0
for i in range(len(m)):
    if m[i]>=a and m[i]<=b:
        continue
    else:
        c+=1
        k.append(m[i])
if c>0:
    print(*k)
else:
    print(-1)