class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        lis = list(num)
        flag = 0
        for i in range(len(num)):
            k = int(num[i:i+1])
            if change[k] > k:
                lis[i] = str(change[k])
                flag = 1
            elif flag==1 and change[k]<k:
                break
        
                
        return ''.join(lis)
            