n=int(input())
arr=list(map(int,input().split()))
for j in range(1,max(arr)+1):
    l=0
    for i in range(0,len(arr)):
        if arr[i]%j==0:
            l+=1
    if l==len(arr):
        R=j
print(R)
