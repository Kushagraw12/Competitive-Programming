#KUSHAGRA WADHWA
# 669; DIV 2; QUES A

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s0 = 0
    s1 = 0
    for i in range(n):
        if a[i] == 0:
                s0 += 1
        else:
                s1 += 1
        if s0 >= s1:
                print(s0)
                for j in range(s0):
                        print("0 ", end = "")
        else:
                if (s1 & 1):
                        s1 -= 1
                print(s1)
                for j in range(s1):
                        print("1 ", end = "")
                print()
