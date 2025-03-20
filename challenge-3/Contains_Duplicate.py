"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.
"""

class Solution:
    def containsDuplicate(self, nums):
        hash_set=set()
        for num in nums:
            if num in hash_set:
                return True
            else:
                hash_set.add(num)
        return False

duplicate = Solution()
print(duplicate.containsDuplicate([1,2,3,1]))
print(duplicate.containsDuplicate([1,2,3,4]))


                
