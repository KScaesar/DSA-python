import bisect
from typing import List


# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.v3(numbers, target)

    def v1(self, numbers: List[int], target: int) -> List[int]:
        # O(N^2)
        size = len(numbers)
        for i in range(size):
            n1 = numbers[i]
            n2 = target - n1
            for j in range(i + 1, size):
                # print(f'j={j} n={numbers[j]}')
                if numbers[j] == n2:
                    return [i + 1, j + 1]
                elif numbers[i] > n2:
                    break

    def v2(self, numbers: List[int], target: int) -> List[int]:
        # O(N*logN)
        size = len(numbers)
        for i in range(size - 1):
            n1 = numbers[i]
            n2 = target - n1

            # https://docs.python.org/3/library/bisect.html
            # all(val < x for val in a[lo : i]) for the left side and
            # all(val >= x for val in a[i : hi]) for the right side.
            # the insertion point will be before (to the right of) any existing entries
            j = bisect.bisect_right(numbers, n2, lo=i + 1)
            # print(f'[i,j]=[{i},{j}] n1={n1} n2={n2}')
            if numbers[j - 1] == n2:
                return [i + 1, j]

    def v3(self, numbers: List[int], target: int) -> List[int]:
        # O(N)
        l = 0
        r = len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            elif total > target:
                r -= 1


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([2, 3, 4], 6))
    print(Solution().twoSum([-1, 0], -1))
    print(Solution().twoSum([5, 25, 75], 100))
