class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low = 0
        res = 0
        counter = {}

        for i in range(len(fruits)):
            counter[fruits[i]] = counter.get(fruits[i], 0) + 1

            while len(counter) > 2:
                counter[fruits[low]] -= 1
                if counter[fruits[low]] == 0:
                    del counter[fruits[low]]
                low += 1

            res = max(res, i - low + 1)

        return res