import collections
import heapq
from typing import List


class Solution:
    # https://leetcode.com/problems/top-k-frequent-elements/

    # 本題也可以用 quickly partition 的解法
    # 時間複雜度可達到 O (N)
    # 找出最高頻率的前k個
    # https://haogroot.com/2020/12/01/top_k_element/
    # https://selfboot.cn/2016/09/01/lost_partition/
    # https://leetcode.com/problems/top-k-frequent-elements/solutions/646157/top-k-frequent-elements/

    def topKFrequent_quickly(self, nums: List[int], k: int) -> List[int]:

        # 完全忘了 partition 怎麼實做, 需要哪些參數
        # 可以參考
        # 0215_Kth_Largest_Element_in_an_Array
        def partition1(freq_pair, left, right) -> int:
            pivot_v = freq_pair[left]
            while left < right:
                while left < right and pivot_v[1] >= freq_pair[right][1]:
                    right -= 1
                freq_pair[left] = freq_pair[right]

                while left < right and pivot_v[1] < freq_pair[left][1]:
                    left += 1
                freq_pair[right] = freq_pair[left]
            freq_pair[left] = pivot_v
            return left

        freq_dict = dict()
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        freq_pair = [(num, freq) for num, freq in freq_dict.items()]

        left = 0
        right = len(freq_pair) - 1
        while True:
            pivot_idx = partition1(freq_pair, left, right)
            if pivot_idx + 1 == k:
                return [freq_pair[i][0] for i in range(pivot_idx + 1)]
            elif pivot_idx + 1 > k:
                right = pivot_idx - 1
            elif pivot_idx + 1 < k:
                left = pivot_idx + 1

    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)
        freq_min_heap = []  # 重點: 求最高頻率, 用 min_heap, 維持固定大小, 而不是用 max_heap
        for i in range(len(nums)):
            freq[nums[i]] += 1

        for key, f in freq.items():
            heapq.heappush(freq_min_heap, (f, key))

            # 重點 heap 維持 容量 k
            # 這樣的話 heappush 的時間複雜度 只會有 logK
            # 整體 變成 N*logK
            if len(freq_min_heap) > k:
                heapq.heappop(freq_min_heap)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(freq_min_heap)[1])

        return ans


if __name__ == '__main__':
    print(Solution().topKFrequent_heap([1, 1, 1, 2, 2, 3], 2))
    print(Solution().topKFrequent_quickly([1, 1, 1, 2, 2, 3], 2))
