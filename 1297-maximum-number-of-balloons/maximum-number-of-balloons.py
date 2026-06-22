class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = [0] * 26

        for i in text:
            count[ord(i) - ord('a')] += 1

        return min(count[ord('b') - ord('a')],
            count[ord('a') - ord('a')],
            count[ord('l') - ord('a')] // 2,
            count[ord('o') - ord('a')] // 2,
            count[ord('n') - ord('a')])
