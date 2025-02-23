"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

 

Constraints:

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.
"""


def single_number_v1(nums):
    counter = {}
    for elem in nums:
        if counter.get(elem, False):
            counter.pop(elem)
        else:
            counter[elem] = True
    return list(counter.keys())[0]


def single_number_v2(nums):
    if len(nums) < 2:
        return nums[0]
    result = nums[0]
    for elem in nums[1:]:
        result ^= elem
    return result


print(single_number_v1([1, 2, 3, 1, 3]))
