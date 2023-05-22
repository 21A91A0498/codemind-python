n=int(input())
l=list(map(int,input().split()))
k=l
for i in range(len(l)):
    s=str(l[i])
    s=int(s[::-1])
    k[i]=s
print(*k)