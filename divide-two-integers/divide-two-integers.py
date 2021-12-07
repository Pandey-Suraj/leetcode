from math import floor,ceil
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        ans = int(dividend/divisor)

        if -2**31 <= ans <= 2**31 - 1:
            return ans
        elif ans>2**31-1:
            return 2**31-1
        else:
            return ans