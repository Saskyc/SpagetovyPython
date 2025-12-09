class Solution:    
    def isPalindrome(self, x: int) -> bool:
        m = str(x)
        cis = len(m)
        
        for i in range(cis // 2):
            if m[i] != m[cis - i - 1]:
                return False
            
        return True

print(int(2.5))
print(Solution().isPalindrome(585))
print(Solution().isPalindrome(123))
print(Solution().isPalindrome(231))
print(Solution().isPalindrome(123321))

"""
#Trying from both sides

class Solution:    
    def isPalindrome(self, x: int) -> bool:
        m = str(x)
        cis = len(m)
        for i in range(int((cis / 2) - (cis % 2) / 2)):
            if m[i] != m[cis - (i + 1)]:
                return False
            
        return True
"""

"""
#Reversing string and then checking it

class Solution:    
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reversed : str = ""
        
        for i in range(len(x)):
            reversed += x[len(x) - (i + 1)]
        
        return reversed == x

"""