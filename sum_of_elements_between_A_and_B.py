n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
sum=0
for i in arr:
    if i in range(a,b+1):
        sum+=i
print(sum)