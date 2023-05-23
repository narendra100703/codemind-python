for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    z=0
    for i in range(1,a+1):
        if(d==z):
            break
        if(i%b==0 and i%c==0):
            continue
        elif(i%b==0 or i%c==0):
            z+=1
    if(z>=d):
        print("Win")
    else:
        print("Lose")