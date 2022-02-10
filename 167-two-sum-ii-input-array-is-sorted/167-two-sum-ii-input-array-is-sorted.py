class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)-1
        l,r = 0,n
        while(l<r):
            mid = (l+r)//2
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1,r+1]
            if total > target:
                r = r-1
            elif total < target:
                l = l + 1
        