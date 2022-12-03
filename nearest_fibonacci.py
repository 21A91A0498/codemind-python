n=int(input())
p=n
a=0
b=1
for i in range(n):
    c=a+b
    a=b
    b=c
    if c>=n:
        break
    k=c
w=c
m=abs(p-k)
t=abs(w-p)
if m>t:
    print(w)
elif m<t:
    print(k)
else:
    print(k,w)