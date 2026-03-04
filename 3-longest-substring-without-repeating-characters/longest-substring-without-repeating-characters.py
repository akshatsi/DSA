class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = ""
        ans = 0

        for i in s:
            if i in a:
                a = a[a.index(i)+1:]   
            a += i
            ans = max(ans, len(a))

        return ans