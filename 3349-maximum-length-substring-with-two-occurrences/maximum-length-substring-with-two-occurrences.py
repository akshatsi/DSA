class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        low = 0
        high = 0
        res = 0
        counter = {}

        for high, ch in enumerate(s):
            counter[ch] = counter.get(ch, 0) + 1
            while counter[ch] > 2:
                counter[s[low]] -= 1
                low += 1

            res = max(res, high - low + 1)

        return res

            
        