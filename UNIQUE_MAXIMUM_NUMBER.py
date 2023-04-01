n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
c=0
m=[]
for i,j in d.items():
    if j==1:
        m.append(i)
        c+=1
if c>0:
    print(max(m))
else:
    print(-1)