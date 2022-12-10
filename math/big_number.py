# https://iter01.com/593290.html


def add(num1: str, num2: str) -> str:
    if len(num1) > len(num2):
        num1, num2 = num2, num1

    len_min = len(num1)
    len_max = len(num2)
    ans = []
    remainder = 0
    up = 0
    i = 0
    for i in range(len_min):
        _sum = int(num1[len_min - i - 1]) + int(num2[len_max - i - 1]) + up
        up = _sum // 10
        remainder = _sum % 10
        # print(up, remainder)
        ans.append(str(remainder))

    for j in range(len_max - len_min):
        _sum = int(num2[len_max - len_min - j - 1]) + up
        up = _sum // 10
        remainder = _sum % 10
        # print(up, remainder)
        ans.append(str(remainder))

    if up:
        ans.append(str(up))

    # ans.reverse()
    return ''.join(ans[::-1])


def subtract(num1: str, num2: str) -> str:
    len1 = len(num1)
    len2 = len(num2)
    if len1 < len2 or (len1 == len2 and num1 < num2):
        num1, num2 = num2, num1

    len_max = len(num1)
    len_min = len(num2)
    i = len_max - 1
    j = len_min - 1

    ans = ''
    up = 0
    remainder = 0

    while i >= 0 or j >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        i -= 1
        j -= 1

        r = n1 - n2 + up
        if r >= 0:
            up = 0
            remainder = r
        elif r < 0:
            up = -1
            remainder = 10 + r

        if i == -1 and \
              r == 0 and \
              len(ans) > 0:  # 避免 2-2=0, 卻沒有出現數字
            pass
        else:
            ans += str(remainder)

    if len1 < len2 or (len1 == len2 and num1 < num2):
        return "-" + ans[::-1]
    else:
        return ans[::-1]


def multiply(num1: str, num2: str) -> str:
    # https://leetcode.com/problems/multiply-strings/
    # https://medium.com/@ChYuan/leetcode-43-multiply-strings-%E5%BF%83%E5%BE%97-medium-c33e8be94919

    len1 = len(num1)
    len2 = len(num2)
    ans = [0] * (len1 + len2)  # 稍微記住, 只需要 len1 + len2 的空間

    for i in range(len1 - 1, -1, -1):
        for j in range(len2 - 1, -1, -1):
            ans[i + j + 1] += int(num1[i]) * int(num2[j])

    for k in range(len(ans) - 1, -1, -1):
        up = ans[k] // 10
        remainder = ans[k] % 10
        ans[k] = remainder
        ans[k - 1] += up

    while len(ans) != 0 and ans[0] == 0:
        ans.pop(0)

    return '0' if len(ans) == 0 else ''.join([str(i) for i in ans])


def divide(num1: str, num2: str) -> str:
    # https://www.youtube.com/watch?v=rI2peJT2Ty8
    # https://www.geeksforgeeks.org/divide-large-number-represented-string/

    q = 0
    n1 = int(num1)
    n2 = int(num2)

    # 超簡易版本
    # 嚴謹版本太複雜了
    # 覺得不會考
    while n1 >= n2:
        n1 -= n2
        q += 1

    return f'{q} {n1}'


if __name__ == '__main__':
    num2 = 12300
    num1 = 12
    print(f'num1={num1} num2={num2}')

    print(f'{"add":>8}: expect = {num1 + num2:>6} actual = {add(str(num1), str(num2)):>6}')
    print(f'{"subtract":>8}: expect = {num1 - num2:>6} actual = {subtract(str(num1), str(num2)):>6}')
    print(f'{"multiply":>8}: expect = {num1 * num2:>6} actual = {multiply(str(num1), str(num2)):>6}')
    print(f'{"divide":>8}: expect = {num1 // num2:>2} {num1 % num2:>2} actual = {divide(str(num1), str(num2)):>6}')
