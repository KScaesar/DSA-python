from tool import debug_helper


def subsets_v1(nums: list[int]) -> list[list[int]]:
    # 靠 python 語言特性 解題

    memo = set()

    @debug_helper
    def backtrace(nums: list[int], track: list[int]):
        nonlocal memo

        key = tuple(sorted(track))
        # if key in memo:
        #     return

        # print(track)
        memo.add(key)

        for i in range(len(nums)):
            # print(i, nums, len(nums))
            v = nums.pop(i)
            track.append(v)
            backtrace(nums, track)
            track.pop()

            # 子集合不需要窮組所有組合, 所以其實不需要進行 insert, 進行此動作, 反而增加運算時間
            # 但是不回覆 nums 的數值, 會造成後續 遞迴 panic
            # 取子集合 最好的方式, 應該用 v2 索引的方式進行
            nums.insert(i, v)

    backtrace(nums, [])
    return [list(x) for x in list(memo)]


def subsets_v2(nums: list[int]) -> list[list[int]]:
    # 算法筆記 p300
    # 回朔法

    result = []

    @debug_helper
    def backtrace(nums: list[int], start: int, track: list[int]):
        nonlocal result
        # print(track)
        result.append(track.copy())

        for i in range(start, len(nums)):
            v = nums[i]
            track.append(v)
            backtrace(nums, i + 1, track)
            track.pop()

    backtrace(nums, 0, [])
    return result


@debug_helper
def subsets_v3(nums: list[int]) -> list[list[int]]:
    # 算法筆記 p300
    # 數學歸納解法

    if len(nums) == 0:
        return [[]]

    sub_answer = subsets_v3(nums[1:])
    result = sub_answer + [x.copy() + [nums[0]] for x in sub_answer]

    # 錯誤作法, 因為 append 沒有回傳值
    # 造成元素為 None
    # result = sub_answer + [x.copy().append(nums[0]) for x in sub_answer]

    return result


if __name__ == '__main__':
    print(subsets_v1([1, 2, 3]), '\n')
    print(subsets_v2([1, 2, 3]), '\n')
    print(subsets_v3([1, 2, 3]), '\n')
