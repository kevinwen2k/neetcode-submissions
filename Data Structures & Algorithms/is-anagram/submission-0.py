class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        for i in range(len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = 0
            hash_s[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in hash_t:
                hash_t[t[i]] = 0
            hash_t[t[i]] += 1

        if len(hash_s.keys()) != len(hash_t.keys()):
            return False

        for c, num in hash_s.items():
            if hash_t.get(c) != num:
                return False

        return True