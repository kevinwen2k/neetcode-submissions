class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        result = 0
        for right, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            while True:
                window_len = right - left + 1
                max_len = max(count.values())
                replacement_needed = window_len - max_len
                if replacement_needed <= k:
                    break

                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result