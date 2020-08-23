import sys
with open("in.txt", 'r') as inp:
        input = inp.readline
        t = int(input())
        for _ in range(t):
                n, k = map(int, input().split())
                w = [int(x) for x in input().split()]

                if max(w) > k:
                        print('-1')
                else:
                        c = 0
                        cur = 0
                        a = 0
              #  print("INT:", w)
                        s = k - w[0]

                        for k in w:
                                while s + k < k:
                                        s += k
                                #print("S", s)
                                if s <= k:
                                        a += 1
                                else:
                                #print(f"MAKING S: {s} 0 for {k}")
                                        s = 0
                        print(a)
