class Solution:
    # https://leetcode.com/problems/valid-anagram/
    def isAnagram_v2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        char_a = ord('a')
        for i in range(len(s)):
            count[ord(s[i]) - char_a] += 1
            count[ord(t[i]) - char_a] -= 1

        for v in count:
            if v != 0:
                return False
        return True

    def isAnagram_v1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = dict()
        for i in range(len(s)):
            c1 = s[i]
            if c1 in count:
                count[c1] += 1
            else:
                count[c1] = 1

            c2 = t[i]
            if c2 in count:
                count[c2] -= 1
            else:
                count[c2] = -1

        for v in count.values():
            if v != 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isAnagram_v1("anagram", "nagaram"))
