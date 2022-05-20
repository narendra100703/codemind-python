n=int(input())
sq_n=n*n
rev=0
while n:
    rev=rev*10+n%10
    n=n//10
sq_rev=rev*rev
a=0
while sq_rev:
    a=a*10+sq_rev%10
    sq_rev//=10
if a==sq_n:
    print(True)
else:
    print(False)    