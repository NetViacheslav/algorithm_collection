from typing import List


class Solution:
    def find_max_average(self, nums: List[int], k: int) -> float:
        sum_arr = 0
        for i in range(k):
            sum_arr += nums[i]

        max_sum = sum_arr
        i = k
        j = 0
        while i < len(nums):
            sum_arr -= nums[j]
            sum_arr += nums[i]
            max_sum = max(max_sum, sum_arr)
            i += 1
            j += 1

        return max_sum / k
