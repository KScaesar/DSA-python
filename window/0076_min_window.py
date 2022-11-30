import collections


def min_window(source: str, target: str) -> str:
    # https://labuladong.github.io/algo/2/20/27/

    current: dict[str, int] = collections.defaultdict(int)
    need: dict[str, int] = collections.defaultdict(int)
    for key in target:
        need[key] = need.setdefault(key, 0) + 1
    must_condition = len(need)

    print(need)
    fast = slow = 0  # 重點: 搜尋區間 [ slow, fast )
    valid_condition = 0

    # 一定要跑完 source 所有字符, 才能知道結果
    # 所以需要 n 和 start
    start = 0
    n = float('inf')

    while fast < len(source):
        key = source[fast]
        fast += 1
        # print(source[slow:fast], len(need))

        if need[key] != 0:
            current[key] += 1
            if current[key] == need[key]:
                valid_condition += 1  # 一个字符已经满足要求

        # 注意 不要用 len(need), 因為 defaultdict 會自動長出 key
        # while valid_condition == len(need):
        while valid_condition == must_condition:  # 多個字符都滿足, 不同題目 收縮條件不一樣

            if fast - slow < n:  # 先判斷本次找到的解, 是否比上次更好
                start = slow
                n = fast - slow

            key = source[slow]
            slow += 1

            if need[key] != 0:
                # current[key] -= 1 錯誤的程式
                # 應該先 判斷是否滿足目標, 再進行減法
                # 感覺需要死記, 想不到合理的邏輯
                #
                # 可以想成
                # 擴展的流程, 先擴展再檢查
                # 收縮的流程, 先檢查再收縮

                if current[key] == need[key]:
                    valid_condition -= 1

                # 窗口中的字符串不再符合要求，left 不再继续移动
                current[key] -= 1  # 進行減法 正確的位置

    return "" if n > len(source) else source[start:start + n]


if __name__ == '__main__':
    sol1 = min_window('ADOBECODEBANC', 'ABC')
    # sol1 = min_window('A', 'A')
    print(f'{min_window.__name__} = {sol1}')
