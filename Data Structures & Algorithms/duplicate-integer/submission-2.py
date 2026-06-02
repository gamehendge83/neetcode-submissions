class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        newDict = list(dict.fromkeys(nums, 0))
        if len(newDict) != len(nums):
            return True
        else: 
            return False