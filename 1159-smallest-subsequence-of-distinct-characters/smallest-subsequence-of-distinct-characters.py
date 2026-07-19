class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        freq = Counter(s)
        seen = set()

        for c in s:
            freq[c] -= 1
            if c in seen:
                continue

            while stack and stack[-1] > c and freq[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)