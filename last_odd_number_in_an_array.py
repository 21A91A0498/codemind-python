n=int(input())
l=list(map(int,input().split()))
oddlast=[]
for i in range(len(l)):
    if l[i]%2:
        oddlast.append(i)
k=max(oddlast)
print(l[k])