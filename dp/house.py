from tool import debug_helper


def house_linear_memo(nums: list[int]) -> int:
    # 算法筆記 p207

    memo: dict[int, int] = dict()

    @debug_helper
    def dp(nums: list[int], start: int) -> int:
        nonlocal memo
        N = len(nums)

        if start >= N:
            return 0

        if start in memo:
            return memo[start]

        memo[start] = max(dp(nums, start + 1), dp(nums, start + 2) + nums[start])
        return memo[start]

    return dp(nums, 0)


if __name__ == '__main__':
    sol1 = house_linear_memo([2, 1, 7, 9, 3, 1])
    print(f'{house_linear_memo.__name__} expect = 12, actual = {sol1}')
