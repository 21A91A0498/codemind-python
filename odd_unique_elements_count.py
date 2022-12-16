n=int(input())
m=list(map(int,input().split()))
k=[]
for i in m:
    if i not in k:
        k.append(i)
c=0
for j in k:
    if j%2:
        c+=1
print(c)