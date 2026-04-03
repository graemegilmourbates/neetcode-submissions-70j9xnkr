class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        while(i<len(nums)):
            j=0
            while(j<len(nums)):
               if i == j: j+=1
               else:
                if(nums[i]+nums[j]==target): return [i,j]
                j+=1
            i+=1

