n=int(input())
m=list(map(int,input().split()))
k=[]
for i in m:
    if i not in k: 
        k.append(i)
for j in k:
    c=0
    for l in m:
        if l==j:
            c+=1
    print(j,c,end=' ')