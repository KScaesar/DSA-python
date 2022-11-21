
def next_greater_element(nums: list[int]) -> list[int]:
    # 算法筆記 p276

    N = len(nums)
    stack = []
    ans = [0]*N

    # 為了模擬環形, 在最右邊的地方, 複製一份 nums
    # 所以 for 執行的個數 變成 兩倍
    # 以下作法就不需要使用額外空間
    for i in range(2*N-1, -1, -1):
        # print(i)
        while len(stack) != 0 and stack[-1] <= nums[i % N]:
            stack.pop()

        ans[i % N] = -1 if len(stack) == 0 else stack[-1]
        stack.append(nums[i % N])

    return ans


if __name__ == '__main__':
    nums = [2, 1, 2, 4, 3]
    print(f'expect=[4, 2, 4, -1, 4], actual={next_greater_element(nums)}\n')
