class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        count1 = {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1

        count2 = {}
        for right, c in enumerate(s2):
            count2[c] = count2.get(c, 0) + 1  # add incoming char

            if right >= n:  # window too wide?
                out = s2[right - n]  # char falling off the left
                count2[out] -= 1
                if count2[out] == 0:
                    del count2[out]  # keep dicts comparable

            if count1 == count2:
                return True

        return False
