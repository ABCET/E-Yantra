T = int(input())
while(T > 0):
    l=int(input())
    a = [int(x) for x in input().split()]
    r=a[::-1]
    for i in range(0,l):
        print(r[i],end=" ")
    print()    
    for i in range(0,l):
        if (i==0) :
            continue
        elif i%3==0:
            print(a[i]+3,end=" ")
    print()
    for i in range(0,l):
        if (i==0) :
            continue
        elif i%5==0:
            print(a[i]-7,end=" ")
    print()
    sum=0
    for i in range(0,l):
        if 3<=i<=7:
            sum+=a[i]
    print(sum)        
    T-=1        
