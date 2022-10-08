T = int(input())
while(T>0):
    n=int(input())
    d={}   
    for i in range(0,n):
        x=input().split()
        d[x[0]]=int(x[1])
    m=int(input())
    for i in range(0,m):
        x=input().split()
        if x[0]=="ADD":
            if x[1] in d:
                d[x[1]]+=int(x[2])
                print("UPDATED Item",x[1])
            else:
                d[x[1]]=int(x[2])
                print("ADDED Item",x[1])
        else:
            if x[1] in d:
                if int(x[2])>d[x[1]]:
                    print("Item",x[1],"could not be DELETED")
                else:
                    d[x[1]]-=int(x[2])
                    print("DELETED Item",x[1]) 
            else:
                print("Item",x[1],"does not exist")
    b=d.values() 
    s=0
    for i in b:
        s+=int(i)  
    print("Total Items in Inventory:",s)  
    T-=1   
