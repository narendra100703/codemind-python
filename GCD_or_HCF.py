def hcf(a,b):
    if a>b:
        s=b
    else:
        s=a
    for i in range(1,s+1):
        if a%i==0 and b%i==0:
            hcf=i
    return hcf       
a,b=map(int,input().split())
print(hcf(a,b))
