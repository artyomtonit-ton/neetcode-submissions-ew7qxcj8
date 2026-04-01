class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct_s = {}
        dct_t = {}

        for ch in s:
            dct_s[ch] = dct_s.get(ch, 0) + 1
        for ch in t:
            dct_t[ch] = dct_t.get(ch, 0) + 1
        
        return dct_s == dct_t