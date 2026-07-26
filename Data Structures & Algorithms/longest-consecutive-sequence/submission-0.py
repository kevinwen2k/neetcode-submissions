class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        arr = sorted(set(nums))       # dedupe + sort
        longest = 1
        current = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1] + 1:   # consecutive → extend run
                current += 1
            else:                          # gap → reset run
                current = 1
            longest = max(longest, current)
        return longest