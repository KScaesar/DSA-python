class Solution:
    # https://leetcode.com/problems/valid-parentheses/
    def isValid(self, s: str) -> bool:
        match = {"(": ")", "[": "]", "{": "}"}
        left = set(match.keys())
        right = set(match.values())
        stack = []

        for v in s:
            if v in left:
                stack.append(match[v])
            elif v in right:
                if len(stack) != 0:
                    if stack.pop() != v:
                        return False
                elif len(stack) == 0:
                    return False

        return len(stack) == 0

    def isValid_fail_v2(self, s: str) -> bool:
        # left right 都是 set, 是隨機排序
        # 因為每次進行 zip 順序都會不同
        # 無法正確配對
        #
        # left = {"(", "[", "{"}
        # right = {")", "]", "}"}
        # match = dict(zip(left, right))

        match = {"(": ")", "[": "]", "{": "}"}
        left = set(match.keys())
        right = set(match.values())
        stack = []
        print(match, left, right, sep="\n")

        for v in s:
            print("stack=", stack)
            if v in left:
                stack.append(match[v])
            elif v in right:
                # 注意檢查 stack 的邊界
                if len(stack) != 0 and stack.pop() != v:
                    return False
                elif len(stack) == 0:  # 第一個 if 判斷的時候, pop 被執行, 造成第二個 if 條件成立
                    return False

        # return True
        # 要檢查是否有剩餘元素
        return len(stack) == 0

    def isValid_fail(self, s: str) -> bool:
        left = {"[": 0, "(": 0, "{": 0}
        for v in s:
            if v in left:
                left[v] += 1
            elif v == "]" and left["["] > 0:
                left["["] -= 1
            elif v == ")" and left["("] > 0:
                left["("] -= 1
            elif v == "}" and left["{"] > 0:
                left["{"] -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    # print(f'{Solution().isValid_fail("([)]")}')
    # print(f'{Solution().isValid("([)]")}')
    print(f'{Solution().isValid("()[]{}")}')
