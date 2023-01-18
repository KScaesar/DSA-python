def combine2(nums: list[int], k: int) -> list[list[int]]:
    def backtrack(nums, cursor, track, k):
        nonlocal ans
        if len(track) == k:
            ans.append(track.copy())
            return

        for i in range(cursor + 1, size):
            v = nums[i]
            track.append(v)
            backtrack(nums, i, track, k)
            track.pop()

    size = len(nums)
    ans = []

    # v2 backtrack
    # cursor 為 n, track 此時為 n 的結果
    #
    # v1 寫法比較簡潔
    for i in range(size):
        backtrack(nums, i, [nums[i]], k)
    return ans


def combine1(nums: list[int], k: int) -> list[list[int]]:
    def backtrack(nums, cursor, track, k):
        nonlocal ans
        if len(track) == k:
            ans.append(track.copy())
            return

        for i in range(cursor, size):
            v = nums[i]
            track.append(v)
            backtrack(nums, i + 1, track, k)
            track.pop()

    size = len(nums)
    ans = []

    # v1 backtrack
    # cursor 為 n, track 此時為 n-1 的結果
    backtrack(nums, 0, [], k)
    return ans


def combine(n: int, k: int) -> list[list[int]]:
    result: list[list[int]] = []

    # @debug_helper
    def backtrack(n: int, k: int, start: int, track: list[int]):
        nonlocal result

        if len(track) == k:
            result.append(track.copy())
            return

        for i in range(start, n + 1):
            track.append(i)
            backtrack(n, k, i + 1, track)  # 注意 不要寫成 backtrack(n, k, start + 1, track)
            track.pop()

    backtrack(n, k, 1, [])
    return result


def main():
    print(combine(4, 2))

    # 比較 v1,v2 的寫法
    print(combine1([1, 2, 3, 4], 2))
    print(combine2([1, 2, 3, 4], 2))


if __name__ == '__main__':
    main()
