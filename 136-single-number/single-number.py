class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fin_dic = {}
        for i in range(len(nums)):
            fin_dic[nums[i]] = fin_dic.get(nums[i], 0) + 1

        return min(fin_dic, key=fin_dic.get)