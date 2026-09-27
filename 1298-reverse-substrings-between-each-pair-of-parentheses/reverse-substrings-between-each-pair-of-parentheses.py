class Solution:
    def reverseParentheses(self, s: str) -> str:
        link = [0] * len(s)
        stk = res = []

        for i,c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                j = stk.pop()
                link[i] = j
                link[j] = i

        dr, i = 1,0 #direction = dr, i = index

        while i < len(s):
            if s[i] >= 'a':
                res.append(s[i])
            else:
                i = link[i]
                dr = -dr

            i += dr

        return ''.join(res)