import numpy as np
with open('timber_sample_input.txt', 'r') as inp:
    input = inp.readline
    with open('sample_output.txt', 'w') as f:
        t = int(input())
        for test in range(1, t + 1):
            n = int(input())
            print("Case #" + str(test) + ": ")
            tree = [[0 for w in range(n)] for j in range(n)]
            for i in range(n):
                tree[i] = input()
                tree[i] = input()
            tree.sort()
            forward = {}
            backward = {}

            for i in range(n):
                start = tree[i]
                end = tree[i] + tree[i + 1]
                forward[end] = max(forward[end], forward[start] + tree[i + 1])

            for i in range(n - 1, 0, -1):
                start = tree[i]
                end = tree[i] - tree[i + 1]
                backward[end] = max(
                    backward[end], backward[start] + tree[i + 1])

            max_len = 0

            for j in forward:
                pos = j
                max_len = max(max_len, forward[pos] + backward[pos])

            for j in backward:
                pos = j
                max_len = max(max_len, forward[pos] + backward[pos])

            print(max_len)
        print()
