from tool import debugHelper


def knapsack_01_backtrace(wt: list[int], val: list[int], W: int) -> int:
    count: int = 0
    space = '  '

    @debugHelper
    def backtrace(wt: list[int], val: list[int], W: int, total: int) -> int:
        nonlocal count
        nonlocal space

        result = total
        # print(f'{space*count}enter wt={wt},W={W},result={result}')

        if len(wt) == 0:
            # print(f'{space*count}return wt={wt},W={W},result={result}')
            return result

        for i, _ in enumerate(wt):
            w = wt.pop(i)
            v = val.pop(i)

            if W-w > 0:
                count = count+1
                result = max(result, backtrace(wt, val, W-w, total+v))
                count = count-1

            wt.insert(i, w)
            val.insert(i, v)

        # print(f'{space*count}return wt={wt},W={W},result={result}')
        return result

    return backtrace(wt, val, W, 0)


if __name__ == '__main__':
    sol1 = knapsack_01_backtrace([2, 1, 3], [4, 2, 3], 4)
    print(f'{knapsack_01_backtrace.__name__} = {sol1}\n')
