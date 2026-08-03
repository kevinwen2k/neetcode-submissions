class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        openers = set(mapping.values())
        for char in s:
            if char in openers:
                stack.append(char)
            elif char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False

        return not stack