class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = {}
        nums.sort()
        length = len(nums)

        for i in range(length - 2):
            first = nums[i]
            left = i + 1
            right = length - 1
            while left < right:
                pair = nums[left] + nums[right]
                if pair < -first:
                    left += 1
                elif pair > -first:
                    right -= 1
                else:
                    result[(first, nums[left], nums[right])] = True
                    left += 1
                    right -= 1

        return [list(k) for k in result.keys()]