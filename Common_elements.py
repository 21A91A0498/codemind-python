n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
ll=[]
for i in l:
    if i in k:
        if i not in ll:
            ll.append(i)
for i in k:
    if i in l:
        if i not in ll:
            ll.append(i)

print(*ll)