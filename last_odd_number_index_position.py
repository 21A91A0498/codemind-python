n=int(input())
l=list(map(int,input().split()))
oddele=[]
for i in range(len(l)):
    if l[i]%2:
        oddele.append(i)
print(max(oddele))