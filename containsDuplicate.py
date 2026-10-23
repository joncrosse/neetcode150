"""
217. Contains Duplicate (Easy)
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return True if any value appears at least twice
in the array, and return False if every element is distinct.

Example 1:
    Input: nums = [1, 2, 3, 1]
    Output: True
    Explanation: The element 1 occurs at indices 0 and 3.

Example 2:
    Input: nums = [1, 2, 3, 4]
    Output: False
    Explanation: All elements are distinct.

Example 3:
    Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    Output: True

Constraints:
    1 <= len(nums) <= 10^5
    -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for i in nums:
            if i in new_set:
                return True
            new_set.add(i)
        return False
        
        
        


if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))                    # expected: True
    print(s.containsDuplicate([1, 2, 3, 4]))                    # expected: False
    print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # expected: True
    print(s.containsDuplicate([1, 5, 6, 3, 7, 4, 8, 2, 4, 2]))  # expected: True
