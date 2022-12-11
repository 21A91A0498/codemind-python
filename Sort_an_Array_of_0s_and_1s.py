n=int(input())
m=list(map(int,input().split()))
a=[]
b=[]
for i in m:
    if i==0:
        a.append(i)
for j in m:
    if j==1:
        b.append(j)
c=a+b
for k in c:
    print(k,end=" ")
