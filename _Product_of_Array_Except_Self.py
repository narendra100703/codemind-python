n = int(input())
arr = list(map(int,input().split()))
for i in range(0,n):
    pdt=1
    for j in range(0,n):
        if i!=j:
            pdt*=arr[j]
    print(pdt,end=" ")