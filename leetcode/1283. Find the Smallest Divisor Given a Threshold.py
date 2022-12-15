import math
from typing import List


class Solution:
    # https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
    # Binary Search Problems
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = 1
        right = max(nums)

        while left <= right:
            mid = left + (right - left) // 2

            # _sum = 0
            # for v in nums:
            #     _sum += math.ceil(v / mid)
            _sum = sum((math.ceil(x / mid) for x in nums))

            if _sum == threshold:
                right = mid - 1
            elif _sum > threshold:
                left = mid + 1
            elif _sum < threshold:
                right = mid - 1

        return left


if __name__ == '__main__':
    print(f'{Solution().smallestDivisor([1, 2, 5, 9], 6)}')
    print(f'{Solution().smallestDivisor([44, 22, 33, 11, 1], 5)}')
