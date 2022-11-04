n=int(input())
l=list(map(int,input().split()))
evenlast=[]
for i in range(len(l)):
    if l[i]%2==0:
        evenlast.append(i)
k=max(evenlast)
print(l[k])