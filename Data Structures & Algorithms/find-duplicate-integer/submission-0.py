class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        prev = 0
        for num in sorted(nums):
            if num == prev:
                return num

            prev = num

        return 0
