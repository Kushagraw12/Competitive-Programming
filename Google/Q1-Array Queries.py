with open("q2in.txt", "r") as inp:
    input = inp.readline
    #import sys
    #input = sys.stdin.readline 
    def rotate_right(arr, n):
        x = arr[n - 1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = x

        return arr

    def rotate_left(arr, n):
        tmp = arr[0]
        for i in range(n-1):
            arr[i] = arr[i+1]
        arr[n-1] = tmp
        return arr
    def q3(arr, k, val):
        arr[k-1] = val
        return arr

    def q4(arr, n):
        arr[n-1] += 1
        return arr 

        
    N = int(input())

    arr = list(map(int,input().strip().split()))

    ql = int(input())

    for _ in range(ql):
        q = list(input().split())
        if q[0] == "Left":
            #print(q[0])
            arr = rotate_left(arr, len(arr))
        elif q[0] == "Right":
            #print(q[0], "OO", q[2])
            arr = rotate_right(arr, len(arr))
        elif q[0] == "Update":
            #print(q[0])
            arr = q3(arr, int(q[len(q) -2]), int(q[len(q)-1]))
        elif q[0] == "Increment":
            arr[int(q[len(q)-1])-1] += 1
            #print("D")
        elif q[0] == "?":
            p = int(q[len(q)-1])
            print(arr[p-1])
