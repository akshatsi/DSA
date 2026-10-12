class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''low = 0
        n = len(s1)
        s1_sort = ''.join(sorted(s1))
        for high in range(len(s2)):
            while high - low + 1 > n:
                low += 1
            if high - low + 1 == n:
                a = ''.join(sorted(s2[low:high + 1]))
            
                if a == s1_sort:
                    return True

        return False'''
        if len(s1) > len(s2):
            return False

        n = len(s1)

        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(n):
            s1_count[ord(s1[i]) - ord('a') ] += 1
            s2_count[ord(s2[i]) - ord('a') ] += 1

        if s1_count == s2_count:
            return True

        for right in range(n, len(s2)):
            s2_count[ord(s2[right]) - ord('a') ] += 1

            left = right - n
            s2_count[ord(s2[left]) - ord('a')] -= 1

            if s1_count == s2_count:
                return True

        return False