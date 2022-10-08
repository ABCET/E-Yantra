for i in range(int(input())):
    x=input().lstrip('@')
    
    for j in(x.split()[:-1]):
        print(len(j),end=",")
    print(len(x.split()[-1]))
