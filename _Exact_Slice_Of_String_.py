n=input()
a=int(input())
b=int(input())
for i in range(len(n)):
    if i in range(a,b+1):
        print(n[i],end='')