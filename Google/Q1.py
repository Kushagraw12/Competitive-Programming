with open("q1in.txt", "r") as inp:
    input = inp.readline

    def testcase():
        return (range(int(input())))

    for _ in testcase():
        