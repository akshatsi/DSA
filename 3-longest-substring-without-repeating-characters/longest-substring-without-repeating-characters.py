class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''a = ""
        ans = 0

        for i in s:
            if i in a:
                a = a[a.index(i)+1:]   
            a += i
            ans = max(ans, len(a))

        return ans'''

        low = 0
        longest = 0
        sett = set()
        for high in range(len(s)):
            while s[high] in sett:
                sett.remove(s[low])
                low += 1
            
            longest = max(longest, high - low + 1)
            sett.add(s[high])

        return longest
            

