n=int(input())
l=list(map(int,input().split()))
evenlist=[]
for i in range(len(l)):
    if l[i]%2==0:
        evenlist.append(i)
print(max(evenlist))