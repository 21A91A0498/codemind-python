n=int(input())
m=list(map(int,input().split()))
s=0
c=0
for i in m:
    s+=i
k=s//len(m)
for j in m:
    if j>=k:
        c+=1
print(c)