n=int(input())
lst=list(map(int,input().split()))[:n]
evensum=[i for i in lst if i%2==0]
print(sum(evensum))