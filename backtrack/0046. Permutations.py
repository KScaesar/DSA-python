from typing import List


class Solution:
    # https://leetcode.com/problems/permutations/

    def permute(self, nums: List[int]) -> List[List[int]]:
        # https://leetcode.com/problems/permutations/solutions/993970/python-4-approaches-visuals-time-complexity-analysis/?orderBy=most_votes

        # 時間複雜度取決於產生每個排列的運算次數。
        # 在這裡，產生每個排列的操作是將剩下的數字插入到軌跡中，直到軌跡的長度等於數列的長度。
        # 在最壞的情況下，每個數字都需要插入軌跡中一次，因此產生排列的操作總共需要執行 n! 次
        #
        # 在最壞的情況下，每個數字都需要插入軌跡中一次，因此產生排列的操作總共需要執行 $n!$ 次。
        # 這是因為一個長度為 $n$ 的排列共有 $n!$ 種不同的可能性，
        # 每一種可能性都需要進行一次操作來得到。因此，總的時間複雜度就是 $O(n!)$。

        # 需要遍歷剩餘的數字，找到還沒有被使用過的數字。
        # 在最壞的情況下，當遍歷到最後一個數字時，每個數字都還沒有被使用過，因此需要遍歷剩餘的數字 (n-1) 次。
        # 接著，在遍歷到倒數第二個數字時，已經有一個數字被使用了，因此只需要遍歷剩餘的數字 (n-2) 次。
        # 以此類推，直到遍歷到第一個數字，只需要遍歷剩餘的數字 1 次。
        # (n−1)+(n−2)+...+1= {n(n−1)} / 2

        # time: O( n! * n(n-1)/2 ) = O(n! * n^2), 此答案是 gpt 的解釋
        # 和 leetcode 解答說法不同

        size = len(nums)
        used = [False] * size
        result = list()

        def backtrack(nums, track, used):
            if len(track) == size:
                result.append(track.copy())
                return

            for i in range(size):
                if not used[i]:
                    track.append(nums[i])
                    used[i] = True
                    backtrack(nums, track, used)
                    track.pop()
                    used[i] = False

        backtrack(nums, [], used)
        return result


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
