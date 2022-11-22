# from backtrace.tool import debugHelper


def permutation(nums: list[int]) -> list[list[int]]:
    result = []

    # @debugHelper
    def backtrace1(nums: list[int], track: list[int]):
        nonlocal result

        if len(nums) == 0:
            result.append(track.copy())
            return

        for i in range(len(nums)):
            # 排除已經選擇的元素 方法3
            # 也可以參考背包問題 can_partition_backtrace
            # 使用 index_record, 紀錄哪元素被選擇
            v = nums.pop(i)

            track.append(v)
            backtrace1(nums, track)
            track.pop()

            nums.insert(i, v)

    def backtrace2(nums: list[int], track: list[int]):
        nonlocal result

        if len(track) == len(nums):
            result.append(track.copy())
            return

        for i in range(len(nums)):
            v = nums[i]

            # 排除已經選擇的元素 方法1
            if track.count(v) != 0:
                continue

            # 排除已經選擇的元素 方法2
            # if v in track:
            #     continue

            track.append(v)
            backtrace2(nums, track)
            track.pop()

    backtrace2(nums, [])
    return result


if __name__ == '__main__':
    print(permutation([1, 2, 3]))
