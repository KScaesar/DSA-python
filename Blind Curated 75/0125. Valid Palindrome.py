import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:

            # 小技巧, 要記住, 可以避免重複計算
            # 將不符合條件的元素, 快速前進
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def isPalindrome_v1(self, s: str) -> bool:
        # lower = set([x for x in range(ord('a'), ord('z') + 1)])
        # upper = set([x for x in range(ord('A'), ord('Z') + 1)])
        # number = set([x for x in range(ord('0'), ord('9') + 1)])
        # charset = lower.union(upper).union(number)
        # data = [ord(x.lower()) for x in s if ord(x) in charset]

        # charset = string.ascii_lowercase + string.ascii_uppercase + string.digits
        charset = string.ascii_letters + string.digits
        data = [x.lower() for x in s if x in charset]

        # print(charset, data)
        left = 0
        right = len(data) - 1
        while left <= right:
            if data[left] != data[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == '__main__':
    # print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("0P"))

    # print([chr(x) for x in range(ord('a'), ord('z') + 1)])
