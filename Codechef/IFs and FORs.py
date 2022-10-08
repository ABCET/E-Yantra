n=int(input())
for i in range(0,n):
    j=int(input())
    for k in range(0,j):
        if k==0:
            print(3,end=" ")
        elif k%2==0:
            print(2*k,end=" ")
        else:
            print(k*k,end=" ")  
    print()              
              
