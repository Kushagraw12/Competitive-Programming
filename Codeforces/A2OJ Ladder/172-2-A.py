# WORD CAPITALIZATION

import sys
input = sys.stdin.readline
s = input()
fir = s[:1].upper()
final = fir + s[1:]
print(final)
