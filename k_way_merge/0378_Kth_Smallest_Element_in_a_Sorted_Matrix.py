import heapq


class Solution:
    # https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        # space complexity O(k)

        n = len(matrix)
        max_heap = []

        for i in range(n):
            for j in range(n):
                heapq.heappush(max_heap, -matrix[i][j])
                if len(max_heap) > k:
                    heapq.heappop(max_heap)

        return -max_heap[0]

    def kthSmallest_binary_search(self, matrix: list[list[int]], k: int) -> int:
        # https://anj910.medium.com/leetcode-378-kth-smallest-element-in-a-sorted-matrix-%E4%B8%AD%E6%96%87-318d52f366af

        # 尋訪 matrix 所有元素時間複雜度 O(n ^ 2)
        # 可以利用行列皆遞增的特性, 比較大的數字會集中在 矩陣右斜對角線 右下角
        # matrix[i][j] 一定小於 matrix[i][j+1] 以及 matrix[i+1][j]
        # 達到 O(長 + 寬) = O(2n) = O(n)
        # https://home.gamer.com.tw/artwork.php?sn=5165011

        n = len(matrix)
        lo = matrix[0][0]
        hi = matrix[n - 1][n - 1]

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            rank = self.search_rank(matrix, mid)  # 目標數字, 在陣列是第幾名
            if rank < k:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo

    def search_rank(self, matrix, target):
        # O(2n)

        n = len(matrix)
        i = n - 1
        j = 0
        rank = 0

        while i >= 0 and j < n:
            if matrix[i][j] <= target:
                rank += (i + 1)
                j += 1
            else:
                i -= 1

        return rank


if __name__ == '__main__':
    obj = Solution()

    sol1 = obj.kthSmallest_binary_search([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)
    print(f'expect=13 actual={sol1}\n')
