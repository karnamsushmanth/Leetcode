#Description
#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
#Example 1:
#Input: nums = [1, 2, 3, 3]
#Output: true
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false


#we will see first the brute force method 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False
#  Time complexity is O(n^2) and space complexity is O(1).

# now we will use data structure which is sorting method

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       nums.sort()
       for i in range(1,len(nums)):
           if nums[i]== nums[i-1]:
               return True  
       return False
   
#    for this approach time complexity is O(nlogn)
#  space complexity is O(1) 
#  if we sacrifice space then we can get better solution that is using hashset

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      seen = set()
      for num in nums:
          if num in seen:
              return True
          seen.add(num)
          return False
      
#    for this approach time complexity is O(n)
#  space complexity is O(n) 

#  Hash set length
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      return len(set(nums))<len(nums)