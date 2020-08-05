def countSubstrings(S):
    N = len(S)
    ans = 0
   # w = []
    for center in range(2 * N - 1):
        left = center / 2
        right = left + center % 2
        while left >= 0 and right < N and S[left] == S[right]:
            # if S[left] not in w:
            ans += 1
            # w.append(S[left])
            left -= 1
            right += 1
    return ans


print(countSubstrings("mokkori"))
