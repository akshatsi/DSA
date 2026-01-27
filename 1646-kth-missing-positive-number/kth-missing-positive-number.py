class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = 0
        curr = 1
        i = 0
        while missing < k:
            if i < len(arr) and arr[i] == curr:
                i += 1
            else:
                missing += 1
                if missing == k:
                    return curr
            curr += 1