class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        sub=0
        for i in range(0,n-1):
            sub=target-nums[i]
            for j in range(i+1,n):
                if(sub==nums[j]):
                    return [i,j]
        