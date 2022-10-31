def get_prfs(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s
a=int(input())
b=int(input())
if get_prfs(a)==b and get_prfs(b)==a:
    print("Amicable")
else:
    print("Not Amicable")