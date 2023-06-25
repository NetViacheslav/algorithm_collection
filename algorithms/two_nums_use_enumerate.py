from typing import List


class Solution:
    def two_sum_with_enumerate(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for value, index in enumerate(nums):
            diff = target - index
            if diff in dict_nums:
                return [dict_nums[diff], value]
            dict_nums[index] = value
        return

