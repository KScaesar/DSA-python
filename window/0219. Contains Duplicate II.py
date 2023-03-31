from typing import List


class Solution:
    # https://leetcode.com/problems/contains-duplicate-ii/description/

    # Sliding Window 比較關注兩個指針之間的區間 關注窗口中的元素
    # https://hackmd.io/X-jeuBQaR7amGQfALM2XDQ?view#Sliding-Window-vs-%E9%9B%99%E6%8C%87%E9%87%9D
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 主要分為 5 個部份, 其中 第 3 步驟, 不一定依照順序進行, 需要依照題目判斷
        # 1. fast++, 增大窗口
        # 2. 更新 window 內容
        #
        # 3. 判斷答案
        #
        # 4. slow--, 縮小窗口
        # 5. 更新 window 內容

        # int left = 0, right = 0;
        #
        #     window = {}
        #     left, right = 0, 0
        #     while right < len(s):
        #         value1 = s[right]
        #         right += 1
        #
        #         # 进行窗口内数据的一系列更新
        #         ...
        #
        #         # debug 输出的位置
        #         print("window: [{}, {})".format(left, right))
        #
        #         while window needs shrink:
        #             value2 = s[left]
        #             left += 1
        #
        #             # 进行窗口内数据的一系列更新
        #             ...

        # https://labuladong.github.io/algo/di-ling-zh-bfe1b/wo-xie-le--f02cd/
        # 索引左闭右开区间 [slow, fast) 称为一个 window
        # 直到 window 中的不再符合要求, 開始縮小 window

        size = len(nums)
        slow, fast = 0, 0
        window = set()

        while fast < size:
            # slide window, 要先抓取符號, 因為 index 會 +1
            # 才能避免 更新window 是否符合的時候
            # 取得 index + 1 的數值, 因為可能造成 out of index
            cursor = nums[fast]
            fast += 1

            # 檢查 window
            if cursor in window:
                return True
            window.add(cursor)

            if fast - slow > k:
                window.remove(nums[slow])
                slow += 1

        return False


if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
    print(Solution().containsNearbyDuplicate([0, 1, 2, 3, 2, 5], 3))
