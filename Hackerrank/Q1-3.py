def palindrome(s):
    m = dict()
    n = len(s)

    dv = [[0 for x in range(n + 1)] for x in range(2)]

    s = "@" + s + "#"

    for j in range(2):
        rp = 0
        dv[j][0] = 0

        i = 1
        while i <= n:

            while s[i - rp - 1] == s[i + j + rp]:
                rp += 1

            dv[j][i] = rp
            k = 1
            while (dv[j][i - k] != rp - k) and (k < rp):
                dv[j][i+k] = min(dv[j][i-k], rp - k)
                k += 1
            rp = max(rp - k, 0)
            i += k
    s = s[1:len(s) - 1]

    m[s[0]] = 1
    for i in range(1, n):
        for j in range(2):
            for rp in range(dv[j][i], 0, -1):
                m[s[i - rp - 1: i - rp - 1 + 2 * rp + j]] = 1
        m[s[i]] = 1

    return len(m)


print(palindrome("mokkori"))
