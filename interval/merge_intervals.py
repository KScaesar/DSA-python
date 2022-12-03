def merge_intervals_v1(v: list[list[int]]) -> list[list[int]]:
    # https://www.educative.io/courses/grokking-coding-interview-patterns-python/m22YrXJwmWO
    v.sort(key=lambda x: x[0])

    result = []
    n = len(v)

    result.append(v[0].copy())
    for i in range(1, n):
        prev_start, prev_end = result[-1]
        current_start, current_end = v[i]
        if prev_end < current_start:
            result.append([current_start, current_end])
        # 注意 條件不是 elif current_start < prev_end and current_end <= prev_end:
        # 需要包含 等於的情況
        elif current_start <= prev_end and current_end <= prev_end:
            result[-1][1] = prev_end
        elif current_start <= prev_end < current_end:
            result[-1][1] = current_end

    return result


def merge_intervals_v2(intervals: list[list[int]]) -> list[list[int]]:
    # leetcode 56
    # https://blog.techbridge.cc/2020/01/16/leetcode-%E5%88%B7%E9%A1%8C-pattern-merge-intervals/
    # https://leetcode.com/problems/merge-intervals/

    n = len(intervals)
    if n < 2:  # 邊界條件要記得處理
        return intervals

    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for i in range(1, n):
        prev_start, prev_end = result[-1]
        current_start, current_end = intervals[i]
        if prev_end < current_start:
            result.append([current_start, current_end])
        else:
            result[-1][1] = max(prev_end, current_end)

    return result


if __name__ == '__main__':
    sol1 = merge_intervals_v1([[1, 5], [4, 6], [6, 8], [11, 15]])
    print(f'{merge_intervals_v1.__name__}: expect=[[1, 8], [11, 15]], actual={sol1}')

    sol2 = merge_intervals_v1([[1, 9], [4, 4], [3, 8]])
    print(f'{merge_intervals_v1.__name__}: expect=[[1, 9]], actual={sol2}')

    sol3 = merge_intervals_v2([[1, 9], [4, 4], [3, 8]])
    print(f'{merge_intervals_v2.__name__}: expect=[[1, 9]], actual={sol3}')
