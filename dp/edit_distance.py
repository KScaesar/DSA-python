def solution_v1_fail(s1, s2) -> int:
    def dp(i, j) -> int:
        nonlocal s1

        # delete
        # 失敗原因, 刪除邏輯應該放置在 s1[i] != s2[j] 來進行
        if i < 0 or j < 0:
            count = i+1 if i >= 0 else j+1
            s1 = s1[count:]
            print(f'delete:\ns1={s1}, i={i}\ns2={s2}, j={j}\n')
            return count

        # skip
        if s1[i] == s2[j]:
            print(f'skip:\ns1={s1}, i={i}\ns2={s2}, j={j}\n')
            return dp(i-1, j-1)
        else:
            # add
            if len(s1) <= len(s2):
                # string not have append method
                # s1.append(s2[j])

                s1 = s1[:i+1]+s2[j]+s1[i+1:]
                print(f'add:\ns1={s1}, i={i}\ns2={s2}, j={j}\n')
                return dp(i, j-1)+1

            # replace
            elif len(s1) > len(s2):
                s1 = "".join((s1[:i], s2[j], s1[i+1:]))
                print(f'replace:\ns1={s1}, i={i}\ns2={s2}, j={j}\n')
                return dp(i-1, j-1) + 1

    return dp(len(s1)-1, len(s2)-1)


def solution_v2(s1, s2) -> int:
    def dp(i, j) -> int:
        if i == -1:
            return j+1
        elif j == -1:
            return i+1

        if s1[i] == s2[j]:
            return dp(i-1, j-1)  # skip
        else:
            return min(
                dp(i, j-1)+1,  # add
                dp(i-1, j)+1,  # delete
                dp(i-1, j-1)+1  # replace
            )

    return dp(len(s1)-1, len(s2)-1)


def solution_v2_memo(s1, s2) -> int:
    memo: dict[tuple[int, int], int] = {}

    def dp(i: int, j: int) -> int:
        # v = memo.get((i, j))
        # if v != None:
        #     print(f'{(i,j)}\n', memo)
        #     return v

        # 確認某個 key 是否存在 dict
        # 用新的寫法比較好
        if (i, j) in memo:
            return memo[(i, j)]

        # base case
        if i == -1:
            return j+1
        elif j == -1:
            return i+1

        if s1[i] == s2[j]:
            memo[(i, j)] = dp(i-1, j-1)  # skip
        else:
            memo[(i, j)] = min(
                dp(i, j-1)+1,  # add
                dp(i-1, j)+1,  # delete
                dp(i-1, j-1)+1  # replace
            )

        return memo[(i, j)]

    return dp(len(s1)-1, len(s2)-1)


# 算法筆記 p133
def solution_v3_table(s1: str, s2: str) -> int:
    dp: list[list[int]] = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

    # base case
    for row in range(len(s1)+1):
        dp[row][0] = row
    for col in range(len(s2)+1):
        dp[0][col] = col

    # s1 != '' and s2 != ''
    for row in range(1, len(s1)+1):
        for col in range(1, len(s2)+1):

            if s1[row-1] == s2[col-1]:
                dp[row][col] = dp[row-1][col-1]
            else:
                dp[row][col] = min(
                    dp[row][col-1]+1,
                    dp[row-1][col]+1,
                    dp[row-1][col-1]+1,
                )

            # print(f'dp[{row}][{col}]={dp[row][col]}')

    # print(dp)
    return dp[len(s1)][len(s2)]


if __name__ == '__main__':
    s1 = 'apply'
    s2 = 'apple'
    # print('v1:', solution_v1_fail(s1, s2))
    # print('v2:', solution_v2(s1, s2))
    print('v2_memo:', solution_v2_memo(s1, s2))
    print('v3_table:', solution_v3_table(s1, s2))

    s1 = 'rad'
    s2 = 'apple'
    # print('v1:', solution_v1_fail(s1, s2))
    print('v2:', solution_v2(s1, s2))
    print('v3_table:', solution_v3_table(s1, s2))
