from typing import List


def frequent_elements(nums: List[int], k: int) -> List[int]:
    count = {}
    frequent = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        frequent[c].append(n)

    res = []
    for i in range(len(frequent) - 1, 0, -1):
        for n in frequent[i]:
            res.append(n)
            if len(res) == k:
                return res
