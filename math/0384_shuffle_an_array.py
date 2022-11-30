import random


class Solution:
    # https://labuladong.github.io/algo/4/32/113/
    #
    # 需要随机选出 k 个不同的位置放雷。你可能说，那在 [0, m * n) 中选出来 k 个随机数
    # 因为你很难保证随机数不重复。如果出现重复的随机数，你就得再随机选一次，直到找到 k 个不同的随机数。
    # 如果 k 比较小 m * n 比较大，那出现重复随机数的概率还比较低
    # 但如果 k 和 m * n 的大小接近，那么出现重复随机数的概率非常高，算法的效率就会大幅下降

    def __init__(self, nums: list[int]):
        self.__nums = nums

    def reset(self) -> list[int]:
        return self.__nums

    # 第一个解决方案，我们可以换个思路
    # 避开「在数组中随机选择 k 个元素」这个问题，把问题转化成「如何随机打乱一个数组」
    # 可以先把这 k 颗雷放在 board 开头，然后把 board 数组随机打乱，这样雷不就随机分布到 board 数组的各个地方了吗
    #
    # 無法解決 在若干元素中随机选择 k 个元素
    def shuffle(self) -> list[int]:
        temp = self.__nums.copy()
        n = len(self.__nums)

        # 生成一个 [i, n-1] 区间内的随机数
        for i in range(n):
            r = random.randint(i, n - 1)
            temp[i], temp[r] = temp[r], temp[i]

        return temp


if __name__ == '__main__':
    sol1 = Solution([1, 2, 4])
    print(f'shuffle = {sol1.shuffle()}')
    print(f'reset = {sol1.reset()}')
