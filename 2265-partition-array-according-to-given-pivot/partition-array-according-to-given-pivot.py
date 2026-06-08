class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        L1 = []
        L2 = []
        L3 = []
        for i in nums:
            if i<pivot:
                L1.append(i)
            elif i>pivot:
                L3.append(i)
            else:
                L2.append(i)
        return L1 + L2 + L3

        