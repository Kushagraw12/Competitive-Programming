import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
        n = int(input())
       # flag = False

        #store = []
        a = list(map(int, input().split()))
        '''
        for i in range(len(a)-3):
            x, y, z = a[i], a[i+1], a[i+2]
            s = (x+y+z) // 2
            area = math.sqrt(s * abs(s-x) * abs(s-y) * abs(s-z) )
            if area <= 0:
                flag = True
                store.append(i)
                store.append(i+1)
                store.append(i+2)'''
            
        if a[0] + a[1] <= a[n-1]:
            print(1, " ", 2, " ", n)
        else:
            print('-1')

