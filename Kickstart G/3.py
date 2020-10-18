#KUSHAGRA WADHWA
import sys
input = sys.stdin.readline


test = int(input())

answer = []

def costSum(wheel, target, N, W, ans):
    s = 0 
    for j in range(w):
        t = 0
        if (wheel[j] > target):
            print(type(wheel[j]), wheel[j])
            t = abs(N - wheel[j] + target)
        else:
            print(type(wheel[j]), wheel[j])
            t = abs(N - target + wheel[j])
        
        temp = min(abs(target - wheel[j]), t)
        s += temp

        if (s > ans): return ans
    
    return s

def output():
    for i in range(test):
        print(f"Case #{i + 1}: {answer[i]}")

for _ in range(test):
    ans = 0
    w, n = map(int, input().split())
    wheel = []
    for i in range(w):
        wheel.append(list(map(int, input().split())))
    for i in range(w):
        ans = min(ans, costSum(wheel, wheel[i], n, w, ans))
    answer.append(ans)