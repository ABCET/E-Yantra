for i in range(int(input())):
    a,b,c=[],[],[]
    for j in range(int(input())):
        x=input().split(" ")
        a.append(x[0])
        b.append(float(x[1]))
    for k in range(len(b)):
        if(b[k]==max(b)):
            c.append(a[k])
    c.sort()
    print(*c,sep="\n")
