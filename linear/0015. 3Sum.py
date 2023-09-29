from typing import List


# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # https://github.com/KScaesar/DSA-python/blob/main/Blind%20Curated%2075/0015.%203Sum.py
        # 之前的寫法是直接找出 2sum 所有可能的解

        # v1 寫法, 受到 167 的影響
        # 每次只找到一組解
        #
        # 缺少考慮的點
        # 1. 同一個 index 可以重複使用, 只要 3sum 的解是不同組合
        # 2. 同一個 index 可以重複使用, used 不適合用在此題目
        # return self.v1_fail(nums)

        # 此題重點:
        # 如何找出一個方法, 如何避免選擇同樣的組合, 但曾經選擇過的數字, 依然可以再次選取
        # 最好的解法, 必須在 2sum 找出所有可能

        return self.v2(nums)

    def v2(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

    def v1_fail(self, nums: List[int]) -> List[List[int]]:
        # sort 後
        # 先扣除 3sum 的 一個數字, 在利用 2sum 找到不重複的數字

        nums.sort()
        size = len(nums)
        used = [False] * size
        result = set()
        ans = []

        i = 0
        while i < size:
            if used[i]:
                i += 1
                continue

            target = -nums[i]
            sub_result = self.twoSum(nums, target, used, i + 1, size - 1)
            # print(f'nums={nums} t={target} sub={sub_result}')
            # print(f'used={used}')
            if sub_result:
                # 如果有找到解, i 不前進, 嘗試尋找是否有下一個解

                r1 = [nums[i], *sub_result]
                r2 = tuple(r1)
                if not r2 in result:
                    result.add(r2)
                    ans.append(r1)

            else:
                i += 1

        print(result)
        return ans

    def twoSum(self, numbers: List[int], target: int, used: List[bool], head: int, tail: int) -> List[int]:
        # O(N)
        l = head
        r = tail
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                if used[l]:
                    l += 1
                elif used[r]:
                    r -= 1
                else:
                    used[l] = True
                    used[r] = True
                    return [numbers[l], numbers[r]]
            elif total < target:
                l += 1
            elif total > target:
                r -= 1

        return []


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
    print(Solution().threeSum([0, 0, 0, 0]) == [[0, 0, 0]])
    print(Solution().threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]])
    print(Solution().threeSum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]])
