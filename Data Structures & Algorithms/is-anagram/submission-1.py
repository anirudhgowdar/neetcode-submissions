class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq, t_freq = {}, {}
        for ch in s:
            if ch not in s_freq:
                s_freq[ch] = 0
            else:
                s_freq[ch] += 1

        for ch in t:
            if ch not in t_freq:
                t_freq[ch] = 0
            else:
                t_freq[ch] += 1

        return s_freq == t_freq