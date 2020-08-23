with open("in2.txt", 'r') as inp:
        input = inp.readline
        t = int(input())
        for _ in range(t):
                n = int(input())
                c = 0
                X = []
                Y = []
                for i in range(n):
                        x , y = input().split()
                        X.append(x)
                        Y.append(Y)
                while n >=3:
                        c += n
                        n = int(n/2)
                print(c)
