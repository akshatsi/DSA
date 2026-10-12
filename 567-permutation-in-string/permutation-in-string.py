class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        low = 0
        n = len(s1)
        s1_sort = ''.join(sorted(s1))
        for high in range(len(s2)):
            while high - low + 1 > n:
                low += 1
            if high - low + 1 == n:
                a = ''.join(sorted(s2[low:high + 1]))
            
                if a == s1_sort:
                    return True

        return False


