class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = {}
        st = {}

        for i in s:
            if i in ss:
                ss[i] += 1
            else:
                ss[i] = 1

        for i in t:
            if i in st:
                st[i] += 1
            else:
                st[i] = 1
                
        return ss == st        