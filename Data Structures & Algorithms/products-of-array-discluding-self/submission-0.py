class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        result = []
        for i, num in enumerate(nums):
            new_list = nums.copy()
            new_list.remove(num)
            result.append(math.prod(new_list))
            
        return result