n = int(input())
arr = list(map(int,input().split()))
a=int(input())
sum=0
for i in arr:
    if i in range(0,a+1):
        sum+=i
print(sum)        