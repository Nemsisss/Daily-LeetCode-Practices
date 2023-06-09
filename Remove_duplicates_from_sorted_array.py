class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        temp= set(nums)
        for i, num in enumerate(sorted(temp)):
            nums[i]=num
            
        return len(temp)
    
# an alternate solution from someone else (two-pointer approach)    
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         c=1
#         for i in range(1,len(nums)):
#             if nums[i]!=nums[i-1]:
#                 nums[c]=nums[i]
#                 c+=1
#         return c
