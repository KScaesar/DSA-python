import collections
from typing import List


class Solution:
    # https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
    # Binary Search Problems
    # https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/solutions/769703/python-clear-explanation-powerful-ultimate-binary-search-template-solved-many-problems/?orderBy=most_votes
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1

        memo = collections.defaultdict(list)
        for i in range(n):
            memo[bloomDay[i]].append(i)

        mapper_bloom_day = []
        for d, index in memo.items():
            mapper_bloom_day.append({"day": d, "index_set": index})
        mapper_bloom_day.sort(key=lambda x: x["day"])
        # print("mapper", mapper_bloom_day)

        left = 0
        right = len(mapper_bloom_day) - 1
        while left <= right:
            mid = left + (right - left) // 2
            current = self.what_many_bouquets(mapper_bloom_day, mid, n, k)
            # print(mid, left, right, current, k)
            if current == m:
                # 錯誤作法
                # 實在稿不清楚, 何時用 左側邊界
                # 何時用 相等
                #
                # return mapper_bloom_day[mid]["day"]
                right = mid - 1
            elif current < m:
                left = mid + 1
            elif current > m:
                right = mid - 1

        return mapper_bloom_day[left]["day"]

    def what_many_bouquets(self, mapper_bloom_day, mapper_index, n, k) -> int:
        bloom = [False] * n
        for i in range(mapper_index + 1):
            for j in mapper_bloom_day[i]["index_set"]:
                bloom[j] = True
        # print(bloom)

        count_k = 0
        count_bouquet = 0
        for i in range(0, n):
            if not bloom[i]:
                count_k = 0
                continue

            count_k += 1
            if count_k == k:
                count_k = 0
                count_bouquet += 1

        return count_bouquet


if __name__ == '__main__':
    print(f'{Solution().minDays([1, 10, 3, 10, 2], 3, 1)}')
    print(f'{Solution().minDays([1, 10, 3, 10, 2], 3, 2)}')
    print(f'{Solution().minDays([7, 7, 7, 7, 12, 7, 7], 2, 3)}')
