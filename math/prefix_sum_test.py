import collections


# 趨勢 2023-01-20 線上測驗第三題
# 給一個字串, 求最長偶數次數的子字串

# https://www.geeksforgeeks.org/number-substrings-count-character-k/

# prefix sum
# 要求某段連續區間的值 所用的技巧
# https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-48c1d/xiao-er-me-f69af/

def code3_v3(data: str, require_times) -> int:
    # 從 v2 的寫法
    # 擴展得到的想法
    #
    # 但是此作法, 限制 require_times <= 10

    size = len(data)
    prefix_cnt = [0] * 26

    # key   = prefix_cnt
    # value = index
    memo = dict()

    # base
    memo["".join([str(v) for v in prefix_cnt])] = -1

    ans = 0
    for idx in range(size):
        c = ord(data[idx]) - ord('a')
        prefix_cnt[c] = (prefix_cnt[c] + 1) % require_times
        prefix = "".join([str(v) for v in prefix_cnt])

        if prefix not in memo:
            memo[prefix] = idx
        else:
            # print(f' idx={idx}, memo={memo}\n')
            ans = max(ans, idx - memo[prefix])

    return ans


def code3_v2(data: str) -> int:
    # 只能用在 求偶數次數的情境

    # 如果兩個prefix xor 一樣
    # 代表他們中間都會是偶數個
    #
    # x1 = a1 xor a2 xor a3
    # x2 = a1 xor a2 xor a3 xor a4 xor a5
    # 如果x1 == x2 代表 a4 xor a5 == 0

    # a到z共26個字
    # 每一個字 占一個bit共26bits
    # int 32bit可以放得下
    # 然後偶數個,可以用(全部)xor 來測試

    size = len(data)
    prefix = 0
    memo = dict()
    memo[0] = -1
    ans = 0

    for idx in range(size):
        c = ord(data[idx]) - ord('a')
        prefix ^= (1 << c)
        if prefix not in memo:
            memo[prefix] = idx
        else:
            ans = max(ans, idx - memo[prefix])

    return ans


def code3_v1(data: str) -> int:
    def window_ok(data, left, right) -> bool:
        if right > len(data):
            return False

        window = collections.defaultdict(int)
        for i in range(left, right):
            c = data[i]
            window[c] += 1

        # 每個字符的出現次數, 是否都是 偶數
        return len([k for k, v in window.items() if v % 2 != 0]) == 0

    ###

    size = len(data)
    ans = 0
    for start in range(size):
        for _len in range(1, size + 1):
            if ans >= _len or _len % 2 == 1:
                continue

            if window_ok(data, start, start + _len):
                # print(data[start:start + _len])
                ans = _len
    return ans


def test_code3_success():
    testcase = [
        (("bdaaadadb",), 6),
        (("bdaaadadb", 2), 6),

        (("bdaa",), 2),
        (("bdaa", 2), 2),

        (("abacb",), 0),
        (("abacb", 2), 0),

        (("abcabc",), 6),
        (("abcabc", 2), 6),

        (("abcabcabc", 3), 9),
        (("caacc", 3), 0),
        (("caacca", 3), 6),
        (("aaac", 3), 3),
    ]

    for param, expected in testcase:
        if len(param) == 1:
            assert code3_v1(*param) == expected
            assert code3_v2(*param) == expected
        else:
            assert code3_v3(*param) == expected
