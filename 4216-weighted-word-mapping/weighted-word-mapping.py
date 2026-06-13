class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""

        for word in words:
            word_weight = 0
            for ch in word:
                word_weight += weights[ord(ch) - ord('a')]

            rem = word_weight % 26
            res += chr(ord('z') - rem)

        return res