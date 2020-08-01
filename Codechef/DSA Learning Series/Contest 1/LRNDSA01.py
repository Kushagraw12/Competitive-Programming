# KUSHAGRA WADHWA
# REVERSE THE NUMBER

t = int(input())

numbers = []
for i in range(t):
    number = int(input())
    numbers.append(number)

for i in range(t):
    reverse = 0
    while numbers[i] > 0:
        remainder = numbers[i] % 10
        reverse = reverse * 10 + remainder
        numbers[i] = numbers[i] // 10
    print(reverse)
