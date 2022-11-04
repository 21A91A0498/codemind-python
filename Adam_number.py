n=int(input())
s=n*n
m=(str(n)[::-1])
x=int(m)
z=x*x
p=(str(z)[::-1])
y=int(p)
if y==s:
    print(True)
    #print(p,s)
else:
    print(False)