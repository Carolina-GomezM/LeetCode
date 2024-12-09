from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        i = 0
        j = 1
        k = 2
        res = 0
 
        while(True):
            if k == len(nums) and j == len(nums)-1:
                i = i+1
                j = i+1
                k = j+1
                if k == len(nums) and j == len(nums)-1 and i == len(nums)-2:
                    return res
                    
            if nums[i] != nums[j]:
                if nums[j] != nums[k] and nums[i] != nums[k]:
                    res = res+1
                    k = k+1
                    if k == len(nums):
                        j = j+1
                        k = j+1
                else:
                    k = k+1
                    if k == len(nums):
                        j = j+1
                        k = j+1
            else:
                j = j+1
                k = j+1 


        