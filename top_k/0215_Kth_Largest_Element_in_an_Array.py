import heapq


class Solution:
    # https://leetcode.com/problems/kth-largest-element-in-an-array/description/
    # https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/60294/solution-explained/?orderBy=most_votes
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # 成功
        # 但以 heap 來說
        # 不是最佳解, 請看 v2
        # 此解法 時間 空間 都比 單純 sort 還爛

        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        ans = None
        for _ in range(k):
            ans = -heapq.heappop(max_heap)

        return ans

    def findKthLargest_v2(self, nums: list[int], k: int) -> int:
        # https://blog.techbridge.cc/2020/04/12/leetcode-%E5%88%B7%E9%A1%8C-pattern-top-k-elements/
        #
        # O(nlogk)
        # 如果 n 比 k 大很多很多，隨時只需要維持 heap 裡面的排序就好
        # 因為 heap 只有 k 個 element，所以維持這個排序所需要的 O(logk) 時間相對就很少

        # 錯誤1: heap 底層的 list 必須為 空陣列, 不然 heap 插入會有錯誤
        # max_heap = [0] * k

        # 錯誤2: 求第 k 大的數目, 應該使用 min_heap, 反之用 max_heap
        # max_heap = []

        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            print(min_heap)

            # 順序不能錯, 一定是先 push, 再檢查長度
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

    def findKthLargest_v3(self, nums: list[int], k: int) -> int:
        # 如果想要更好的效率, 利用 快速排序 partition 概念
        # https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/60294/Solution-explained/

        target = k - 1
        left = 0
        right = len(nums) - 1

        while True:
            position = self.partition_v2(nums, left, right)
            if position == target:
                return nums[target]
            elif position > target:
                right = position - 1
            elif position < target:
                left = position + 1

    def partition_v1(self, nums, left, right) -> int:
        # https://www.youtube.com/watch?v=Dk9tpG6Jhso&list=PLl-9hEcChubjZRzIoSdACioC2Fsx-JBup&t=120s

        pivot = nums[left]

        # 仔細想想條件 是 < 還是 <=
        # 可以想成 要保留最後一個位置進行 nums[left]=pivot
        # 所以相等的時候 不進行動作
        while left < right:
            while left < right and pivot >= nums[right]:  # 遞減數列用 pivot >= nums[right]
                right -= 1
            nums[left] = nums[right]

            while left < right and pivot < nums[left]:
                left += 1
            nums[right] = nums[left]

        nums[left] = pivot
        return left

    def partition_v2(self, nums, left, right) -> int:
        # https://www.youtube.com/watch?v=duln2xAZhBA&t=294s

        # pivot_idx 表示最终分割点的位置，初始值为 left - 1，表示初始时还没有数据比枢纴值小
        pivot_v = nums[right]
        pivot_idx = left - 1

        # 每当遍历到一个数据时，都会比较它和枢纴值的大小
        # 如果遍历到的数据比枢纴值小，就将它和 pivot_idx 指向的数据交换位置
        # 就能保证 pivot_idx 后面的数据都比枢纴值小
        for cursor in range(left, right):  # 不會執行到最後一個元素, 因為當成 pivot_v 了
            # 遞減 nums[cursor] >= pivot_v, 想要減少交換的情況, 可以沒有 等於 條件
            # 遞增 nums[cursor] <= pivot_v
            if nums[cursor] > pivot_v:
                pivot_idx += 1
                nums[cursor], nums[pivot_idx] = nums[pivot_idx], nums[cursor]

        pivot_idx += 1
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        return pivot_idx


if __name__ == '__main__':
    obj = Solution()

    sol1 = obj.findKthLargest_v3([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    print(f'expect=4 actual={sol1}')
