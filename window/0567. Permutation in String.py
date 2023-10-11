from collections import Counter


# https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.v3(s1, s2)

    def v3(self, s1: str, s2: str) -> bool:
        s1_target = dict(Counter(s1))
        s1_target_len = len(s1)
        s2_total = {}

        size = len(s2)
        l, r = 0, 0
        while r < size:
            char_r = s2[r]
            r += 1
            s2_total[char_r] = s2_total.get(char_r, 0) + 1

            # 這才是正確的條件, 要能夠組合出目標, 至少長度要相同
            if r - l == s1_target_len:
                print(f'l={l} r={r}, is_satisfy_target: s2_total={s2_total}')
                if self.is_satisfy_target(s1_target, s2_total):
                    return True

                char_l = s2[l]
                l += 1
                s2_total[char_l] -= 1
                if s2_total[char_l] == 0:
                    s2_total.pop(char_l)

        return False

    def v2_fail(self, s1: str, s2: str) -> bool:
        # 跟 v1 相比, 利用 s2_total_key 減少一次 N1 查詢
        # 錯誤的滿足條件
        # O(N2 * N1)

        s1_target = dict(Counter(s1))
        s2_total = {}
        s2_total_key = 0

        # print(f's1={s1} s2={s2}')
        print(f's1_target={s1_target}')

        size = len(s2)
        l, r = 0, 0
        while r < size:
            char_r = s2[r]
            r += 1
            if char_r in s1_target and s2_total.get(char_r) is None:
                s2_total_key += 1
            s2_total[char_r] = s2_total.get(char_r, 0) + 1

            # print(f'l={l} r={r}, is_gte_target: s2_total={s2_total}')
            # 錯誤的滿足條件
            while s2_total_key == len(s1_target) and s2_total[char_r] >= s1_target[char_r]:

                print(f'l={l} r={r}, is_equal_target: s2_total={s2_total}')
                if self.is_satisfy_target(s1_target, s2_total):
                    return True

                char_l = s2[l]
                l += 1
                s2_total[char_l] -= 1
                if s2_total[char_l] == 0:
                    s2_total.pop(char_l)
                if char_l in s1_target and s2_total.get(char_l) is None:
                    s2_total_key -= 1

        return False

    def v1(self, s1, s2):
        # O(N2 * N1 * N1)

        s1_target = dict(Counter(s1))
        s2_total = {}

        # print(f's1={s1} s2={s2}')
        # print(f's1_target={s1_target}')

        size = len(s2)
        l, r = 0, 0
        while r < size:
            char_r = s2[r]
            r += 1
            s2_total[char_r] = s2_total.get(char_r, 0) + 1

            # print(f'l={l} r={r}, is_gte_target: s2_total={s2_total}')
            while self.is_gte_target(s1_target, s2_total):

                print(f'l={l} r={r}, is_equal_target: s2_total={s2_total}')
                if self.is_satisfy_target(s1_target, s2_total):
                    return True

                char_l = s2[l]
                l += 1
                s2_total[char_l] -= 1
                if s2_total[char_l] == 0:
                    s2_total.pop(char_l)

        return False

    def is_gte_target(self, s1_target, s2_total) -> bool:
        for k, v in s1_target.items():
            if s2_total.get(k, 0) < v:
                return False
        return True

    def is_satisfy_target(self, s1_target, s2_total) -> bool:
        for k, v in s1_target.items():
            if s2_total.get(k, 0) != v:
                return False
        return len(s2_total) == len(s1_target)


if __name__ == '__main__':
    # print(Solution().checkInclusion("ab", "eidbaooo") == True)
    print(Solution().checkInclusion("trinitrophenylmethylnitramine", "dinitrophenylhydrazinetrinitrophenylmethylnitramine") == True)
