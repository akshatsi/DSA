class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        seen = set()
        for i in range(len(digits)):
            if digits[i] == 0:
                continue

            for j in range(len(digits)):
                if i == j:
                    continue
            
                for u in range(len(digits)):
                    if u == i or u == j:
                        continue

                    if digits[u] % 2 != 0:
                        continue

                    num = digits[i]*100 + digits[j] * 10 + digits[u]
                    seen.add(num)

        return len(seen)