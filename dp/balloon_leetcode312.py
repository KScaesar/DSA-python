from tool import debugHelper


def maxScore_backtrace(nums: list[int]) -> int:
    # https://labuladong.github.io/algo/3/28/92/
    # 算法筆記 p187

    result = float('-inf')

    # 虛擬氣球
    nums.insert(0, 1)  # left
    nums.append(1)  # right

    @debugHelper
    def backtrace1(nums: list[int], score: int):
        nonlocal result
        N = len(nums)

        # 條件不要搞錯 N == 0, 是錯誤條件
        # N == 2, 代表剩下兩個虛擬氣球
        if N == 2:

            # 要把所有的元素用光
            # 才能得到最終結果
            # 所以此函數 backtrace
            # 不需要回傳值
            # 只需要在結束條件 收集結果
            result = max(result, score)
            return

        for i in range(1, N-1):
            point = nums[i-1]*nums[i]*nums[i+1]

            c = nums.pop(i)
            backtrace1(nums, score+point)
            nums.insert(i, c)

    backtrace1(nums, 0)

    return result


if __name__ == '__main__':
    sol1 = maxScore_backtrace([3, 1, 5, 8])
    print(f'{maxScore_backtrace.__name__} = {sol1}\n')
