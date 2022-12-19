n=int(input())
if n>=0:
    print(int(str(n)[::-1]))
elif n<0:
    a=n*-1
    b=int(str(a)[::-1])
    print(-(b))
    