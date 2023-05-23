def palindrome(n):
    s=str(n)
    k=s[::-1]
    if k==s:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if palindrome(i):
        c+=1
print(c)