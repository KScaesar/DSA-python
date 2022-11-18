from tool import debugHelper


def knapsack_01_backtrace(wt: list[int], val: list[int], W: int) -> int:
    # count: int = 0
    # space = '  '

    # @debugHelper
    def backtrace(wt: list[int], val: list[int], W: int, total: int) -> int:
        # nonlocal count
        # nonlocal space

        result = total
        # print(f'{space*count}enter wt={wt},W={W},result={result}')

        if len(wt) == 0:
            # print(f'{space*count}return wt={wt},W={W},result={result}')
            return result

        for i, _ in enumerate(wt):
            w = wt.pop(i)
            v = val.pop(i)

            if W-w > 0:
                # count = count+1
                result = max(result, backtrace(wt, val, W-w, total+v))
                # count = count-1

            wt.insert(i, w)
            val.insert(i, v)

        # print(f'{space*count}return wt={wt},W={W},result={result}')
        return result

    return backtrace(wt, val, W, 0)


def can_partition_backtrace(nums: list[int]) -> bool:
    N = len(nums)
    W = sum(nums)//2

    # @debugHelper
    def backtrace1(N: int, W: int, pick: list[int]) -> bool:
        nonlocal nums

        if N >= 0 and W == 0:
            return True
        elif N == 0 and W != 0:
            return False

        for i in range(N):
            if nums[i] > W:
                continue

            w = nums.pop(i)
            pick.append(w)
            result = backtrace1(N-1, W-w, pick)
            nums.insert(i, w)

            if result:
                return True
            else:
                pick.pop()

        return False

    # @debugHelper
    def backtrace2(index_record: dict[int, bool], W: int, pick: list[int]) -> bool:
        nonlocal nums
        N = len(nums)

        if N >= 0 and W == 0:
            return True
        elif N == 0 and W != 0:
            return False

        for i in range(N):
            w = nums[i]
            if index_record.get(i, False) or w > W:
                continue

            pick.append(w)
            index_record[i] = True
            result = backtrace2(index_record, W-w, pick)
            index_record[i] = False

            if result:
                return True
            else:
                pick.pop()

        return False

    # return backtrace1(N, W, [])
    return backtrace2(dict(), W, [])


if __name__ == '__main__':
    sol1 = knapsack_01_backtrace([2, 1, 3], [4, 2, 3], 4)
    print(f'{knapsack_01_backtrace.__name__} = {sol1}\n')

    sol2 = can_partition_backtrace([1, 6, 4, 9])
    # sol2 = can_partition_backtrace([1, 5, 11, 5])
    print(f'{can_partition_backtrace.__name__} = {sol2}\n')

    # sol3 = can_partition_backtrace([1, 3, 2, 8])
    # print(f'{can_partition_backtrace.__name__} = {sol3}\n')
