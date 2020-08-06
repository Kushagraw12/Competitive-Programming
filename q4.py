import sys
#input = sys.stdin.readline


def possiblerotation(n, arr, s):
    #print(n, len(arr))
    #val = arr[s-1]
    #dest = 0
    q = 0
    flag = False
    #print(val, arr[s-1])
    if 0 <= s <= n:
        # print(s)
        if arr[s-1] == 0:
            flag = True
            # print(flag)
    if 0 <= s <= n:
        # print(flag)
        for i in range(n):
            if arr[i] == 0:
                #dest = arr[i]
                q = i
        if q < s-1:
            #print(val, arr[s-1])
            while arr[s-1] != 0 and n > 0:
                #print(val, arr[s-1])
                if 0 <= s <= n:
                    s -= arr[s-1]
                    if arr[s-1] == 0:
                        flag = True
                n -= 1
        if q > s-1:
            #print(val, arr[s-1])
            while arr[s-1] != 0 and n > 0:
                #print(val, arr[s-1])
                if 0 <= s <= n:
                    s += arr[s]
                    if arr[s] == 0:
                        flag = True
                    n -= 1

        if flag:
            return 1
        else:
            return 0


def printpossiblerotation(n, arr, s):
    if possiblerotation(n, arr, s) == 1:
        print('YES')
    else:
        print('NO')


# with open("q4input.txt", "r") as inp:
 #   input = inp.readline
t = int(input())
for i in range(t):
    len = int(input())
    arr = list(map(int, input().split()))
    s = int(input())
    printpossiblerotation(len, arr, s)

'''5
4 2 0 2 3
4'''
