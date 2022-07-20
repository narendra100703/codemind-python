def pal(n):
    t=n
    s=str(n)
    s=s[::-1]
    s=int(s)
    if(s==n):
        return True
    return False
n=int(input())
c=0
k=list(map(int,input().split()))
for i in range(n):
    if(pal(k[i])==True):
        c+=1
print(c)