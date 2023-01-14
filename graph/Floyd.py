from typing import List


class Solution:
    # 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
    # https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

    # https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/solutions/490312/java-c-python-easy-floyd-algorithm/

    # https://www.youtube.com/watch?v=XzmTiO3j6p0

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Time O(N^3)
        # Space O(N^2)

        dp = [[float('inf')] * n for _ in range(n)]  # node1 to node 的距離
        middle = [[-1] * n for _ in range(n)]  # node1 to node2 的中轉點, 一開始都不存在, 所以 -1

        # base case
        for e in edges:
            _from, to, d = e
            dp[_from][to] = dp[to][_from] = d  # 無向圖的寫法
            # dp[_from][to] = d  # 有向圖的寫法
        for i in range(n):
            dp[i][i] = 0

        for k in range(n):
            for node1 in range(n):
                for node2 in range(n):
                    dist = dp[node1][k] + dp[k][node2]
                    if dist < dp[node1][node2]:
                        dp[node1][node2] = dist
                        middle[node1][node2] = k

        smallest_cnt = n
        ans = 0
        for node1 in range(n):
            cnt = 0
            for node2 in range(n):
                if node1 != node2 and dp[node1][node2] <= distanceThreshold:
                    cnt += 1
            if smallest_cnt >= cnt:
                smallest_cnt = cnt
                ans = node1

        # tool.print_matrix(dp)
        # tool.print_matrix(middle)
        return ans


if __name__ == '__main__':
    print(Solution().findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))

    # https://youtu.be/XzmTiO3j6p0?t=194
    # print(Solution().findTheCity(3, [[0, 2, 13], [0, 1, 6], [2, 0, 5], [1, 0, 10], [1, 2, 4]], 4))
