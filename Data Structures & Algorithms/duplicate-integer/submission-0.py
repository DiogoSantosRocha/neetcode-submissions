class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seens = {}

        for num in nums:
            if num in seens:
                seens[num] += 1
                return True
            else:
                seens[num] = 1
                
                
        return False