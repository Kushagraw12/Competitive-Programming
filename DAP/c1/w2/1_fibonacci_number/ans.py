import sys
import time
with open('input.txt', 'r') as inp:
    start_time = time.time()
    input = inp.readline
    def solve(n):
        n1 = 0
        n2 = 1
        arr = []
        for i in range(n-1):
            arr.append(n1 + n2)
            n1, n2 = n2, n1 + n2
        return max(arr)
    for _ in range(int(input())):
        n = int(input())
        print(solve(n))
    print(f"Time Taken:{time.time()-start_time}")