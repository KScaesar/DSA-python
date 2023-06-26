# 台積電 測驗 code2

maps = {
    'a': 1,
    'b': 1,
    'c': 2,
    'd': 2,
    'e': 2,
    'f': 3,
    'g': 3,
    'h': 3,
    'i': 4,
    'j': 4,
    'k': 4,
    'l': 5,
    'm': 5,
    'n': 5,
    'o': 6,
    'p': 6,
    'q': 6,
    'r': 7,
    's': 7,
    't': 7,
    'u': 8,
    'v': 8,
    'w': 8,
    'x': 9,
    'y': 9,
    'z': 9,
}


def countSubstrings_v3(input_str):
    # prefix sum
    # https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-48c1d/xiao-er-me-03265/

    size = len(input_str)
    prefix = [0 for _ in range(size + 1)]  # prefix[0] = 0，便于计算累加
    for i in range(1, size + 1):
        prefix[i] = prefix[i - 1] + maps[input_str[i - 1]]

    cnt = 0
    for i in range(size):
        for n in range(1, size + 1):
            if i + n <= size:
                total = prefix[i + n] - prefix[i]
                if total % n == 0:
                    cnt += 1

    return cnt


def countSubstrings_v2(input_str):
    # O(n^2)
    size = len(input_str)
    cnt = 0
    for i in range(size):
        total = 0
        for j in range(i, size):
            n = j - i + 1
            total += maps[input_str[j]]
            if total % n == 0:
                cnt += 1

    return cnt
    pass


def countSubstrings_v1(input_str):
    # O(n^3)
    size = len(input_str)
    cnt = 0
    for i in range(size):
        for j in range(i, size):
            n = j - i + 1
            total = sum([maps[c] for c in input_str[i:i + n]])
            # print(f'{input_str[i:i + n]:>8} total={total:>3} n={n :>} ')
            if total % n == 0:
                cnt += 1

    return cnt


if __name__ == '__main__':
    print(countSubstrings_v1('asdf'))
    print(countSubstrings_v2('asdf'))
    print(countSubstrings_v3('asdf'))
    print()
    print(countSubstrings_v1('bdh'))
    print(countSubstrings_v2('bdh'))
    print(countSubstrings_v3('bdh'))
