from tool import sort_nested


# 找出 nums 中
# 有哪些組合, 可以相加得到 target
# 一個元素只能被用一次
# 回傳 value pair

def two_sum_v4(nums, target) -> list[list[int]]:
    # 和 v3 邏輯相同
    # 只是換一個寫法

    nums.sort()
    size = len(nums)
    left = 0
    right = size - 1
    ans = []
    while left < right:
        _sum = nums[left] + nums[right]
        if _sum == target:
            if len(ans) == 0:
                ans.append([nums[left], nums[right]])
            elif len(ans) != 0 and ans[-1] != [nums[left], nums[right]]:
                ans.append((nums[left], nums[right]))
            right -= 1
        elif _sum > target:
            right -= 1
        elif _sum < target:
            left += 1
    return ans


def two_sum_v3(nums, target) -> list[list[int]]:
    # 有排序, 效能比 v2 更好

    nums.sort()  # 沒進行排序的話, 很難最佳化 過濾重複 的問題
    left = 0
    right = len(nums) - 1
    ans = []

    # 因為要求 sum 累加的元素, 不能是同一個
    # 等號的情況, 代表指向同一個元素, 違反題目規則
    while left < right:
        left_v = nums[left]
        right_v = nums[right]
        _sum = left_v + right_v
        if _sum == target:
            ans.append([left_v, right_v])

            # 為了找到下一個解, 可以選擇 left or right 到下一個元素
            while right >= 0 and right_v == nums[right]:  # 跳過重複
                right -= 1

        elif _sum > target:
            while right >= 0 and right_v == nums[right]:  # 跳過重複 記得要確保 index 在邊界內
                right -= 1
        elif _sum < target:
            while left < len(nums) and left_v == nums[left]:  # 跳過重複
                left += 1

    return ans


def two_sum_v2(nums, target) -> list[list[int]]:
    # 有排序, 配合剪枝判斷, 效能好
    # 但比較難得知, 原本的 nums, 如何組成 target
    # 也就是要求 返回 index 的話, v2 不適合
    def dfs(nums, cursor, _sum, track):
        nonlocal ans
        if _sum == target and len(track) == 2:
            ans.append([nums[i] for i in track])
            return
        elif len(track) >= 2:
            return
        elif _sum > target:
            return

        for i in range(cursor, len(nums)):
            # 剪枝判斷
            if i > cursor and nums[i - 1] == nums[i]:
                continue

            v = nums[i]
            track.add(i)
            dfs(nums, i + 1, _sum + v, track)
            track.remove(i)

    nums.sort()
    ans = []
    dfs(nums, 0, 0, set())
    return ans


def two_sum_v1(nums, target) -> list[list[int]]:
    # 沒有排序, 適合用來求原本數列的 index
    # 如何組成 target

    # 如果要求返回 index
    # 用 hashtable 實作, 效能更好
    # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0015.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.md#%E6%80%9D%E8%80%83%E9%A2%98
    # https://programmercarl.com/0001.%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C.html#%E6%80%9D%E8%B7%AF

    # @debug_helper
    def dfs(nums, cursor, _sum, track, used):
        nonlocal ans
        if _sum == target and len(track) == 2:
            if track & used:
                return
            used |= track
            ans.append([nums[i] for i in track])
            return
        elif len(track) >= 2:
            return
        elif _sum > target:
            return

        for i in range(cursor, len(nums)):
            if track & used:
                continue

            v = nums[i]
            track.add(i)
            dfs(nums, i + 1, _sum + v, track, used)
            track.remove(i)

    ans = []
    dfs(nums, 0, 0, set(), set())
    return ans


def test_two_sum():
    nums = [1, 2, 3, 1, 2]
    target = 4
    assert sort_nested(two_sum_v1(nums, target)) == [[1, 3], [2, 2]]
    assert sort_nested(two_sum_v2(nums, target)) == [[1, 3], [2, 2]]
    assert sort_nested(two_sum_v3(nums, target)) == [[1, 3], [2, 2]]
    assert sort_nested(two_sum_v4(nums, target)) == [[1, 3], [2, 2]]
