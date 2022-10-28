t=int(input())
i=1
while i<=t:
    n=int(input())
    temp=n**0.5
    if int(temp)==temp:
        print(True)
    else:
        print(False)