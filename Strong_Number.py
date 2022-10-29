n=int(input())
sum=0
temp=n
while n:
    d=n%10
    p=1
    while d:
        p=p*d
        d=d-1
    sum=sum+p
    n=n//10
if temp==sum:
    print('The number',temp,'is a strong number')
else :
    print('The number',temp,'is not a strong number')
