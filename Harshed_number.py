n=int(input())
sum=0
temp=n
while temp!=0:
    r=temp%10
    sum+=r
    temp=temp//10
if n%sum==0:
    print(True)
else:
    print(False)