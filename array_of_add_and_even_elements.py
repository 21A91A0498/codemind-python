n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i%2:
        a.append(i)
    if i%2==0:
        b.append(i)
a.extend(b)
print(*a)