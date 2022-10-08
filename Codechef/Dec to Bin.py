for i in range(int(input())):
    x=int(input())
    print("0"*(8-len(bin(x)[2:]))+bin(x)[2:])
