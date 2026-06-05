class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def canPlace(d):
            count = 1 #placing first ball 
            lastBall = position[0] #2nd ball
            for i in range(1, len(position)):
                if position[i] - lastBall >= d:
                    count += 1
                    lastBall = position[i]

                    if count == m:
                        return True
            return False

        low = 1
        high = position[-1] - position[0]
        ans = 0

        while low<= high:
            mid = (high + low) // 2
            if canPlace(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

