# AUTHOR: KUSHAGRA WADHWA

with open('alchemy_input.txt', 'r') as inp:
    input = inp.readline
    with open('alchemy_output.txt', 'w') as f:
        t = int(input())
        for test in range(1, t + 1):
            n = int(input())
            s = input()
            difference = 0
            for i in s:
                if i == "A":
                    difference += 1
                elif i == "B":
                    difference -= 1

            if difference == 1 or difference == -1:
                print('Case #' + str(test) + ": " + "Y", end="", file=f)
            else:
                print('Case #' + str(test) + ": " + "N", end="", file=f)
            print(file=f)
    f.close()
inp.close()
