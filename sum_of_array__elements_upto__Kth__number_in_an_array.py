n=int(input())
arr=list(map(int,input().split()))
a=int(input())
sum=0
for i in range(0,a):
    r=arr[i]%10
    sum+=r
    arr[i]=arr[i]//10
print(sum)    
    