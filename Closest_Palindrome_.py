def palindrome(n):
    m=n
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    if rev==m:
        return True
        
n=int(input())
i=n-1
p=n+1
while i<n:
    if palindrome(i):
        k=i
        break
    i-=1
while p>=n:
    if palindrome(p):
        j=p
        break
    p+=1
l=abs(n-k)
g=abs(n-j)
if l<g:
    print(k)
elif l>g:
    print(j)
elif l==g:
    print(k,j)