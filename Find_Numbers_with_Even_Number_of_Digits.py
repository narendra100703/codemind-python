n=int(input())
arr=list(map(int,input().split()))
c1=0
for i in arr:
    c2=0
    temp=i
    while temp:
        r=temp%10
        c2+=1
        temp=temp//10
    if c2%2==0:
        c1+=1
print(c1)        
    