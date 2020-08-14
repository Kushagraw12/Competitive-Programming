def minStartValue(nums):
        helper = 0
        ans = 1
        
        for num in nums:
            helper += num
            ans = max(ans, 1 - helper)
        
        return ans
        
    
    
n = int(input())
arr = []
for i in range(n):
    k = int(input())
    arr.append(k)
    
print(minStartValue(arr))