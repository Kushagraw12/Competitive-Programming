import sys
input = sys.stdin.readline
t=int(input())
for _ in range(t):
	n = int(input())
	even = 0
	odd = 0
	curr = 0
	maximum = 0
	count = 0
	l = list(map(int,input().split()))
	for i in range(n):
		if l[i] == 1:
			if curr != 0:
				if maximum < curr:
					maximum = curr
					count = 1
				elif maximum == curr:
					count += 1
			curr = 0
		else:
			curr += 1
	if count == 1:
		curr = 0
		possible = False
		for i in range(n):
			if l[i] == 1:
				if curr != 0:
					if maximum != curr and curr >= (maximum // 2) + 1:
						possible = True
						break
				curr = 0
			else:
				curr += 1
	if maximum % 2 != 0:
		if count == 1 and possible == False:
			print("Yes")
		else:
			print("No")
	else:
		print("No")