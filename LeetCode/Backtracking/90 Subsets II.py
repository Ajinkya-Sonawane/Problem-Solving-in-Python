# https://leetcode.com/problems/subsets-ii/
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        arr=[]
        nums.sort()
        def helper(nums,i,arr):
            if i==len(nums):
                #print(arr)
                ans.append(arr[:])
                #print(ans)
                return
            arr.append(nums[i])
            helper(nums,i+1,arr)
            arr.pop()
            #escape from the same element as it will cause similar answers
            while(i+1 < len(nums) and nums[i+1] == nums[i]): 
                i+=1
            helper(nums,i+1,arr)
            return
        helper(nums,0,arr)
        return ans