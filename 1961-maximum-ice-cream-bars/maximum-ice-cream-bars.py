class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        i=0
        n=len(costs)
        while coins>0 and i<n:
            if costs[i]<=coins:
                coins-=costs[i]
                count+=1
                i+=1
            else:
                break
        return count
