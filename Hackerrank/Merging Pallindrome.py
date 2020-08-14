def substring(s, a, b): 
    s1 = "" 

    for i in range(a, b, 1): 
        s1 += s[i] 
  
    return s1 

def allPalindromeSubstring(s): 
    v = [] 

    pivot = 0.0
    while pivot < len(s): 

        palindromeRadius = pivot - int(pivot) 
  

        while ((pivot + palindromeRadius) < len(s) and 
                   (pivot - palindromeRadius) >= 0 and 
                  (s[int(pivot - palindromeRadius)] == 
                   s[int(pivot + palindromeRadius)])): 
             v.append(s[int(pivot - palindromeRadius): 
                        int(pivot + palindromeRadius + 1)]) 
  
             palindromeRadius += 1
  
        pivot += 0.5
    return v 
    
def canFormPalindrome(strr): 

    listt = [] 

    for i in range(len(strr)): 
        if (strr[i] in listt): 
            listt.remove(strr[i]) 
        else: 
            listt.append(strr[i]) 

    if (len(strr)% 2 == 0 and len(listt) == 0 or (len(strr) % 2 == 1 and len(listt) == 1)): 
        return True
    else: 
        return False
        
    
def solve(s1, s2):
    f = False
    d = {}
    d2 = {}
    for i in s1:
        for j in s2:
            ans = i + j
            if canFormPalindrome(ans):
                
                d[ans] = len(ans)
    
    print(max(d, key=d.get))
    
arr = input()
arr2 = input() 
s1 = allPalindromeSubstring(arr)
s2 = allPalindromeSubstring(arr2)
solve(s1, s2)
