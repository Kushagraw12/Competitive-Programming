s = input()
for _ in range(len(s)):
    s = s.replace('--', '2')
for _ in range(len(s)):
    s = s.replace('-.', '1')
for _ in range(int(len(s))):
    s = s.replace('.', '0')
print(s)
