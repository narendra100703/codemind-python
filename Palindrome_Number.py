n=int(input())
while n:
    n-=1
    a=int(input())
    rev=0
    temp=a
    while temp:
        r=temp%10
        rev=rev*10+r
        temp=temp//10
    if rev==a:
        print(True)
    else:
        print('False')