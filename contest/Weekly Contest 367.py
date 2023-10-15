from typing import List


# https://leetcode.com/contest/weekly-contest-367

class Solution:
    # https://leetcode.com/contest/weekly-contest-367/problems/find-indices-with-index-and-value-difference-i/
    def findIndices_Native(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            for j in range(i, size):
                diff_idx = abs(i - j)
                diff_v = abs(nums[i] - nums[j])
                if diff_idx >= indexDifference and diff_v >= valueDifference:
                    return [i, j]
        return [-1, -1]

    def findIndices_v1_fail(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        size = len(nums)
        data = [(i, nums[i]) for i in range(size)]  # index,value
        data.sort(key=lambda x: x[1])
        print(f'{data}')

        l, r = 0, size - 1
        while l <= r:
            l_item = data[l]
            r_item = data[r]
            diff_idx = abs(r_item[0] - l_item[0])
            diff_v = abs(r_item[1] - l_item[1])
            print(f'[{diff_idx},{diff_v}]')
            if diff_idx >= indexDifference and diff_v >= valueDifference:
                ans = [l_item[0], r_item[0]]
                return ans
            elif diff_idx < indexDifference and diff_v >= valueDifference:
                # idx 沒有進行排序, 不知道應該 l+=1 or r-=1
                pass
        return [-1, -1]

    # https://leetcode.com/contest/weekly-contest-367/problems/shortest-and-lexicographically-smallest-beautiful-string/
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        min_len = len(s) + 1
        substring = ""

        cnt: int = 0
        l, r = 0, 0
        size = len(s)
        while r < size:
            if s[r] == "1":
                cnt += 1
            r += 1

            while cnt == k:
                if r - l < min_len:
                    min_len = r - l
                    substring = s[l:r]
                elif r - l == min_len and s[l:r] < substring:
                    substring = s[l:r]

                if s[l] == "1":
                    cnt -= 1
                l += 1

        # print(substring)
        return substring

    def findIndicesII(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # 此題如同第一題, 但要求更好的時間複雜度

        min_v_idx = -1
        min_v = 10 ** 10  # 10^10 用來代表某個極大數字
        max_v_idx = -1
        max_v = -10 ** 10  # -10^10 用來代表某個極小數字

        n = len(nums)
        for i in range(indexDifference, n):
            j = i - indexDifference
            if nums[j] < min_v:
                min_v_idx = j
                min_v = nums[j]
            if nums[j] > max_v:
                max_v_idx = j
                max_v = nums[j]

            if nums[i] - min_v >= valueDifference:
                return [min_v_idx, i]
            if max_v - nums[i] >= valueDifference:
                return [i, max_v_idx]

        return [-1, -1]

    # https://leetcode.com/contest/weekly-contest-367/problems/construct-product-matrix/
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == '__main__':
    # print(Solution().findIndices_Native([5, 1, 4, 1], 2, 4))
    # print(Solution().findIndices_Native([0, 5, 10, 5], 3, 0))

    # print(Solution().shortestBeautifulSubstring("1011", 2) == "11")
    # print(Solution().shortestBeautifulSubstring("110101000010110101", 3) == "1011")

    print(Solution().findIndicesII([5, 1, 4, 1], 2, 4))
    print(Solution().findIndicesII([0, 5, 10, 5], 3, 0))
