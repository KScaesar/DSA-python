import random


class Solution:
    # https://labuladong.github.io/algo/2/20/30/
    # 前缀和技巧 加上 二分搜索详解
    # 能够解决带权重的随机选择算法

    # prefix sum
    # https://hackmd.io/@meyr543/Bk2Nd21AY
    # https://labuladong.github.io/algo/2/20/24/

    def __init__(self, w: list[int]):
        self.w: list[int] = w

        # prefix_sum[i] 记录 nums[0..i-1]
        self.prefix_sum: list[int] = [0] * (len(w) + 1)

        for i in range(1, len(w) + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + w[i - 1]

    def pickIndex(self) -> int:

        # 快速寻找数组中大于等于目标值的最小元素？ 二分搜索算法
        # 随机数 target 应该在什么范围取值？闭区间 [0, target] 还是左闭右开 [0, target) or [0, target]？
        # random 取值 從 1 開始
        target = random.randint(1, self.prefix_sum[-1])

        left = 0
        right = len(self.prefix_sum) - 1  # 注意 right 取值 不是用 len(self.w)

        # 困難點 當目標值不在 array 中
        # 什麼樣的條件 才能跳出 while 迴圈
        #
        # 大于等于目标值的最小元素？
        # 使用搜索 *左侧边界* 的二分搜索
        while left <= right:
            mid = left + (right - left) // 2
            current = self.prefix_sum[mid]
            print(f'cursor={left, mid, right} current={current} target={target}')

            if current == target:
                right = mid - 1  # 搜索左侧边界的二分搜索
            elif current > target:
                right = mid - 1
            elif current < target:
                left = mid + 1

        # 最后对这个索引减一（因为前缀和数组有一位索引偏移），就可以作为权重数组的索引
        return left - 1


if __name__ == '__main__':
    obj = Solution([1, 3])
    for _ in range(10):
        print(f'sol = {obj.pickIndex()}')
