n=int(input())
arr=list(map(int,input().split()))
temp=0
for i in arr:
    if i%2==0:
        temp=i
print(temp)
    