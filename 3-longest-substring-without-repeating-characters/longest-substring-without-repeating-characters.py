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

        l = 0 #left
        longest = 0
        sett = set()
        n = len(s)

        for r in range(n): #right
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            w = r - l + 1
            longest = max(longest,w)
            sett.add(s[r])

        return longest

