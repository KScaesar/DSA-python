from typing import List


class Solution:
    # https://leetcode.com/problems/house-robber-ii/
    def rob(self, nums: List[int]) -> int:
        # 对于一个数组，成环的话主要有如下三种情况
        # 情况一：考虑不包含首尾元素
        # 情况二：考虑包含首元素，不包含尾元素
        # 情况三：考虑包含尾元素，不包含首元素
        # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0213.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DII.md
        #
        # 知道要分三種情境, 但沒想法要如何實做

        size = len(nums)
        if size <= 1:
            return 0 if size == 0 else nums[0]

        dp_head = [0] * size
        dp_tail = [0] * size

        if size >= 1:
            dp_head[0] = nums[0]
        if size >= 2:
            dp_head[1] = max(nums[0], nums[1])

            dp_tail[1] = nums[1]
        if size >= 3:
            dp_tail[2] = max(nums[1], nums[2])

        for i in range(2, size - 1):
            dp_head[i] = max(dp_head[i - 1], dp_head[i - 2] + nums[i])
        for i in range(3, size):
            dp_tail[i] = max(dp_tail[i - 1], dp_tail[i - 2] + nums[i])

        # size 不足, 直接寫-2可能引發錯誤
        # return max(dp_head[- 2], dp_tail[- 1])
        return max(dp_head[size - 2], dp_tail[size - 1])


if __name__ == '__main__':
    print(Solution().rob([1, 2, 3, 1]))
    print(Solution().rob([1, 2, 3]))
