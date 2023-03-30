n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)-1,len(l)//2-1,-1):
    k.append(l[i])
for i in range(0,len(l)//2):
    k.append(l[i])
print(*k)