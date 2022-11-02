n=int(input())
lst=list(map(int,input().split()))[:n]
sumarray=[i for i in lst]
print(sum(sumarray))