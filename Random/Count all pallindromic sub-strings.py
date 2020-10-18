#KUSHAGRA WADHWA
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(19))

def solve(s):
	l = len(s)
	
    # 2 D array
	count = [[0 for i in range(l + 2)]for j in range(l + 2)]

    # Length 1
	for i in range(l):
		count[i][i] += 1
	

	# ALGO
	for x in range(2, l + 1):

		for i in range(l):
			k = (x + i) - 1
			if (k < l):
				if (s[i] == s[k]):
					count[i][k] = (count[i][k - 1] + count[i + 1][k] + 1)
				else:
					count[i][k] = (count[i][k - 1] + count[i + 1][k] - count[i + 1][k - 1])


	return count[0][l - 1]

s = input()
print(solve(s))