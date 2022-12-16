n=int(input())
m=list(map(int,input().split()))
s=0
k=[]
for i in m:
    if i not in k:
        k.append(i)
for j in k:
    s+=j
print(s)