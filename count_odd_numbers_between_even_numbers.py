n=int(input())
lst=list(map(int,input().split()))
count=0
for i in range(1,len(lst)-1):
    if lst[i]%2!=0 and lst[i+1]%2==0 and lst[i-1]%2==0:
        count+=1
print(count)