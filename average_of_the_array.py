n=int(input())
sum=0
lsty=list(map(int,input().split()))[:n]
for i in lsty:
    sum+=i
k=sum/len(lsty)
print('%0.2f'%k)