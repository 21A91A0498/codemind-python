n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
ll=[]
for i in l:
    if i not in k:
        ll.append(i)
for i in k:
    if i not in l:
        ll.append(i)
s=list(set(ll))
print(*ll)