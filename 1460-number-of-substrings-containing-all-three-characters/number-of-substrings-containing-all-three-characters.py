class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = [0,0,0] #list to store frequency of a b c
        low = 0
        high = 0
        res = 0
        for high in range(len(s)):
            freq[ord(s[high]) - ord('a')] += 1
            while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                n = len(s) - high 
                res += n
                freq[ord(s[low])-ord('a')] -= 1
                low += 1

        return res
