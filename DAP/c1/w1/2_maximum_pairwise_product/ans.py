import sys 
input = sys.stdin.readline

def solve(arr):
    arr.sort()
    return (arr[len(arr) - 1] * arr[len(arr) - 2])

n = int(input())
arr = [int(x) for x in input().split()]
print(solve(arr))