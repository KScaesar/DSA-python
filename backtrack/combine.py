from tool import debug_helper


def combine(n: int, k: int) -> list[list[int]]:
    result: list[list[int]] = []

    @debug_helper
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


if __name__ == '__main__':
    main()
