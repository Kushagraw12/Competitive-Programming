import sys
input = sys.stdin.readline

def bin(n):
        if (n > 1):
                bin(n >> 1)
        #print(n & 1, end = "")
        return (n & 1)

t = int(input())
for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        s = 0
       # print(a, "A")
        #print(a[0], "NS")
        #print(bin(a[0]))
        #print("INT:", int(bin(a[1])))
        for i in a:
                if int(bin(i)) % 10 == 0:
                        s += i
        print(s)
