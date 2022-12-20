def rev(n):
    a=int(str(n)[::-1])
    return a
def palin(n):
    a=int(str(n)[::-1])
    if a==n:
        return True
n=int(input())
while n:
    a=n+rev(n)
    if palin(a):
        print(a)
        break
    n=a