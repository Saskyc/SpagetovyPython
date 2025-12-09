class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        h = {}
        k = 0
        
        for i in nums:
            if h.get(i) == None:
                k += 1
            h[i] = 0
        
        return k

print(Solution().removeDuplicates([1, 2, 3, 1, 1, 4, 4, 4]))