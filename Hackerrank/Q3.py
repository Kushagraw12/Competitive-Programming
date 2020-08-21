def meanderingArray(unsorted):
    unsorted.sort()
    n = len(unsorted)
    tmp = n * [None]

    low, top = 0, n - 1

    counter = True

    for i in range(n):
        if counter is True:
            tmp[i] = unsorted[top]
            top -= 1
        else:
            tmp[i] = unsorted[low]
            low += 1

        counter = bool(1-counter)

    for i in range(n):
        unsorted[i] = tmp[i]
    return unsorted


t = [5, 2, 7, 8, -2, 25, 25]
# t.sort()
print(meanderingArray(t))
