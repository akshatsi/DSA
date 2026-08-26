class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)

        left = 0
        ones = 0
        ans = ""

        for right in range(n):

            if s[right] == '1':
                ones += 1

            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            if ones == k:
                temp = left

                while temp < right and s[temp] == '0':
                    temp += 1

                cur = s[temp:right + 1]

                if ans == "" or len(cur) < len(ans) or \
                   (len(cur) == len(ans) and cur < ans):
                    ans = cur

        return ans