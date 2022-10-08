import functools as f
def generate_AP(a1, d, n):
    A=[]
    for i in range(0, n):
        A.append(a1 + i * d)
    return A


# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    T = int(input())
    while(T>0):
        a1,d,n=[int(x) for x in input().split()]
        AP_series = generate_AP(a1, d, n)
        for i in range(0, n):
            print (AP_series[i], end=" ")
        print()
        # Using lambda and map functions, find squares of terms in AP series and print it
        sqr_AP_series = list(map(lambda x: x**2, AP_series))
        for i in range(0, n):
            print (sqr_AP_series[i], end=" ")
        print()    

        # Using lambda and reduce functions, find sum of squares of terms in AP series and print it
        sum_sqr_AP_series = f.reduce(lambda x, y: x+y, [i for i in sqr_AP_series], 0)
        print (sum_sqr_AP_series)
        T-=1
