n,m=map(int,input().split())
i=1
j=1
dupli=n
revs=0
r=0
rev=int(str(n)[::-1])
while i<=m:
    d=rev%10
    revs=revs*10+d
    rev=rev//10
    i+=1
while j<=m:
    k=dupli%10
    r=r*10+k
    dupli=dupli//10
    j+=1
l=int(str(r)[::-1])
print(abs(l-revs))

