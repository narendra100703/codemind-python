n=int(input())
arr=list(map(int,input().split()))
for i in range(0,n-1):
    if arr[i+1]>arr[i]:
        print('no')
        break
else:
    print('yes')    