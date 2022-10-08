for i in range(int(input())):
    x=input()
    if(x.upper()==x[::-1].upper()):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
