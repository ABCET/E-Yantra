import math
def compute_distance(x1, y1, x2, y2):

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print('Distance: %.2f' % distance)




if __name__ == '__main__':
    T = int(input())
    while(T > 0):
        x1,y1,x2,y2 = [int(x) for x in input().split()]
        compute_distance(x1, y1, x2, y2)
        T=T-1
