class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = False

        if len(s) == len(t):
            flag = True

            ss = sorted(s)
            st = sorted(t)

            for i in range(len(ss)):
                if ss[i] != st[i]:
                    flag = False

        return flag
        