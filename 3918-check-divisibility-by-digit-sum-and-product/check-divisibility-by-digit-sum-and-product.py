class Solution:
    def checkDivisibility(self, n: int) -> bool:
        d_sum = 0
        prod = 1
        for i in str(n):
            a = int(i)
            d_sum += a

            prod *= a

        if n % (d_sum + prod) == 0:
            return True

        else:
            return False
