import collections
import queue


class Solution:
    # https://leetcode.com/problems/top-k-frequent-elements/
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        memo = collections.defaultdict(int)
        for num in nums:
            memo[num] += 1

        # 如果要節省 heap 的 空間
        # 可以使用 quick sort 概念的 partition
        # 利用遞迴求解
        # https://haogroot.com/2020/12/01/top_k_element/
        # https://selfboot.cn/2016/09/01/lost_partition/

        hq = queue.PriorityQueue()
        for num, count in memo.items():
            hq.put((-count, num))

        return [hq.get()[1] for _ in range(k)]


if __name__ == '__main__':
    obj = Solution()

    sol1 = obj.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(f'expect=[1,2] actual={sol1}')
