class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        length = len(cleaned)
        right = length - 1
        for i in (range(length//2)):
            if cleaned[i] != cleaned[length - 1 - i]:
                return False

        return True