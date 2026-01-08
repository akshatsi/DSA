class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])

        return res