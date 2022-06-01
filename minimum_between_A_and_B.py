a=int(input())
arr=list(map(int,input().split()))
arr.sort()
m,n=map(int,input().split())
minn=n
c=0
for i in arr:
    if i>=m and i<=n:
        if minn>i:
            minn=i
            c+=1
if  c<=0:
    print(-1)
else:
    print(minn)