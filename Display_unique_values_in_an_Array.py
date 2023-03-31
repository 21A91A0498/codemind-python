n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
c=0
k=[]
for i,j in d.items():
    if j==1:
        k.append(i)
        c+=1
if c>0:
    print(*k)
else:
    print(-1)
        