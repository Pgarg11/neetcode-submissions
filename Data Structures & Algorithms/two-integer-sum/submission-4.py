
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hp={}

        for i,m in enumerate(nums):
            hp[m]=i
        for i,m in enumerate(nums):
            sub=target-nums[i]
            if sub in hp and hp[sub]!=i:
                return[i,hp[sub]]
        return []