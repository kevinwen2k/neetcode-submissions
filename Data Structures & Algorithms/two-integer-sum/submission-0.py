class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            prior = target - num
            if prior in hm:
                return [hm[prior], i]
            
            hm[num] = i

        return []