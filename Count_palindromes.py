def pali(i):
    rev=0
    temp=i
    while temp>0:
        r=temp%10
        rev=rev*10+r
        temp=temp//10
    if i==rev:
        return True
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if(pali(i)):
        c+=1
print(c)        

        