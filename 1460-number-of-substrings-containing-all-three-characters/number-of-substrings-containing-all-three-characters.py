class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = [0,0,0]
        l = 0
        r = 0
        res = 0
        for r in range(len(s)):
            freq[ord(s[r])- ord('a')] += 1 #converts to ascii easy to map without dictionary
            while  freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                n = len(s) - r
                res += n
                freq[ord(s[l])- ord('a')] -= 1
                l+= 1

        return res
