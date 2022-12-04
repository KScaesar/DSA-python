class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        # 442. Find All Duplicates in an Array
        # https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
        # https://haogroot.com/2020/11/26/cyclic_sort-leetcode/

        n = len(nums)
        i = 0
        result = []
        while i < n:
            # for i in range(n):
            # print(nums, i)

            # because nums are in the range [1, n]
            value = nums[i] - 1

            # 注意這是錯誤條件, 會進入無窮迴圈
            # 不是找尋當下 index 的 數值, 是否符合 當下的 index
            # if value != i and value >= 0:
            #
            # 而是找尋 當下 index 的數值, 是否符合 數值指向的數值
            if value != (nums[value] - 1) and value >= 0:
                nums[i], nums[value] = nums[value], nums[i]
            else:
                i += 1

        for i in range(n):
            if i != (nums[i] - 1):
                result.append(nums[i])

        return result

    def findDisappearedNumbers_v1(self, nums: list[int]) -> list[int]:
        # 448. Find All Numbers Disappeared in an Array
        # https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

        # 沒有限制空間複雜度的話
        # 用 v2 比較好

        # 維持 v1 效果, 但減少 swap, 用 v3
        n = len(nums)

        ans = []
        i = 0
        while i < n:
            v = nums[i] - 1
            if v != nums[v] - 1:
                nums[v], nums[i] = nums[i], nums[v]
            else:
                i += 1

        for i in range(n):
            if i != nums[i] - 1:
                ans.append(i + 1)

        return ans

    # 448. Find All Numbers Disappeared in an Array
    def findDisappearedNumbers_v2(self, nums: list[int]) -> list[int]:
        # https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
        n = len(nums)
        memo = set(nums)
        return [x + 1 for x in range(n) if x + 1 not in memo]

    def findDisappearedNumbers_v3(self, nums: list[int]) -> list[int]:
        # https://blog.techbridge.cc/2020/02/16/leetcode-%E5%88%B7%E9%A1%8C-pattern-cyclic-sort/
        # Index as hash key 解法

        n = len(nums)

        for i in range(n):
            target = abs(nums[i]) - 1

            # 第一次看到此數字 才可以進入邏輯
            if nums[target] > 0:
                # 把 index 當 key, 標示為負號, 表示有找到
                nums[target] *= -1

            # 沒有處理重複數字的情況
            # v = abs(nums[i]) - 1
            # nums[v] *= -1

            # 錯誤, 這題要好好想想 正確邏輯是什麼!
            # v = nums[i] - 1
            # if v != nums[v] - 1 and v >= 0:
            #     nums[v] *= -1

        # print(nums)
        return [i + 1 for i in range(n) if nums[i] > 0]


if __name__ == '__main__':
    obj = Solution()
    print(f'{obj.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])}\n')
    print(f'{obj.findDisappearedNumbers_v3([4, 3, 2, 7, 8, 2, 3, 1])}\n')
