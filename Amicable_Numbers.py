a=int(input())
b=int(input())
c=1
sum=0
while c<=a//2:
    if a%c==0:
        sum+=c
    c+=1
if sum==b:
    print('Amicable')
else:
    print('Not Amicable')