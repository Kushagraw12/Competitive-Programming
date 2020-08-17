def solve(A):
    openCount = 0
    closeCount = 0
    ans = 0
    for i in A:
        if i == "<":
            openCount += 1
        else:
            closeCount +=1
        if openCount == closeCount:
            ans = openCount + closeCount
        elif openCount < closeCount:
            return ans
    return ans

#import sys
#input = sys.stdin.readline
t = int(input())
for test in range(t):
    s = list(input())
    print(solve(s))