class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        maxi = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] <= 1:
                maxi = max(maxi, arr[i])
            else:
                arr[i] = arr[i-1] + 1
                maxi = max(maxi, arr[i])
        return maxi