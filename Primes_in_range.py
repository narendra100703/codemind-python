def prime(m):
    if m==1:
        return False
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            return False
    return True    
m=int(input())
n=int(input())
p=0
while m<=n:
    if prime(m):
        p+=1
    m+=1
print(p)