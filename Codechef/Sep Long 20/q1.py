import sys
import numpy as np
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def transpose(matrix, end):
        begin = 0
        result = [[matrix[j][i] for j in range(begin, len(matrix) ) ] for i in range( end  )]
        return result

for _ in range(int(input())):
        n = int(input())
        matrix = [[]]
        for i in range(n):
                matrix.append(list(map(int, input().split())))
        print(matrix)

        for l in range(1, len(matrix)):
                m = transpose(matrix[1:l], l) + matrix[l + 1:len(matrix)]
                print(f"M: {l} ", m)


        r = [[matrix[j][i] for j in range(1, len(matrix))] for i in range(len(matrix[1]))]
        print(r)
