from typing import List


class Solution:
    # https://leetcode.com/problems/largest-time-for-given-digits/

    # https://github.com/halfrost/LeetCode-Go/tree/master/leetcode/0949.Largest-Time-for-Given-Digits

    def largestTimeFromDigits_v2(self, arr: List[int]) -> str:
        # 直接判斷數字更直覺
        # 跟數字大小有關的限制, 最好還是直接用 數字比較
        # 不要用一個一個位數比較

        ans = []

        def dfs(arr, track, used):
            nonlocal ans

            track_size = len(track)
            if track_size == 2:
                hour = 10 * track[0] + track[1]
                if hour > 23:
                    return
            elif track_size == 4:
                minute = 10 * track[2] + track[3]
                if minute > 59:
                    return

            if len(track) == len(arr):
                if ans < track:
                    ans = track.copy()
                    return

            for i in range(len(arr)):
                if used[i]:
                    continue

                v = arr[i]
                used[i] = True
                track.append(v)
                dfs(arr, track, used)
                used[i] = False
                track.pop()

        dfs(arr, [], [False] * len(arr))

        if len(ans) == 0:
            return ""

        ans.insert(2, ":")
        return "".join([str(v) for v in ans])

    def largestTimeFromDigits_v1(self, arr: List[int]) -> str:
        # 把這題想成 排列問題
        # 需要排除特定條件, 才會滿足最終答案

        # 容易忽略的地方
        # h2 會隨著 h1 的數值, 最大數值限制會有所不同

        # hour1 [0,2]
        # hour2 [0,3] or [0,9]
        # minute1 [0,5]
        # minute2 [0,9]
        limits = {
            "h1": "2",
            "h2_small": "3", "h2_large": "9",
            "m1": "5",
            "m2": "9"
        }

        ans = ""

        def dfs(arr, track, used):
            nonlocal ans

            track_size = len(track)
            limit = -1
            if track_size == 1:
                limit = limits["h1"]
            elif track_size == 2:
                limit = limits["h2_small"] if track[0] == "2" else limits["h2_large"]
            elif track_size == 3:
                limit = limits["m1"]
            elif track_size == 4:
                limit = limits["m2"]
            if track_size != 0 and track[-1] > limit:
                return

            if len(track) == len(arr):
                candidate = "".join(track)
                if ans < candidate:
                    ans = candidate
                    return

            for i in range(len(arr)):
                if used[i]:
                    continue

                v = str(arr[i])
                used[i] = True
                track.append(v)
                dfs(arr, track, used)
                used[i] = False
                track.pop()

        dfs(arr, [], [False] * len(arr))

        if len(ans) == 0:
            return ans
        return ans[:2] + ":" + ans[2:]

    def largestTimeFromDigits_fail2(self, arr: List[int]) -> str:
        # 失敗原因
        # 前面的時間欄位 都選最佳解
        # 可能造成 後面欄位 產生無效數值
        # [2,0,6,6] 以此作法 會找出 20:6X 到 第三個數字就無效
        # 但實際上 可以有一個答案是 "06:26"

        # 容易忽略的地方
        # h2 會隨著 h1 的數值, 最大數值有所不同

        # hour1 [0,2]
        # hour2 [0,3] or [0,9]
        # minute1 [0,5]
        # minute2 [0,9]
        limits = {
            "h1": 2,
            "h2_small": 3, "h2_large": 9,
            "m1": 5,
            "m2": 9
        }

        def find_target(arr, limit) -> int:
            for v in range(limit, -1, -1):
                for i in range(len(arr)):
                    if v == arr[i]:
                        arr.pop(i)
                        return v
            return -1

        ans = ["", "", ":", "", ""]
        for i in range(len(ans)):
            limit = -1
            if i == 0:
                limit = limits["h1"]
            elif i == 1:
                limit = limits["h2_small"] if ans[0] == "2" else limits["h2_large"]
            elif i == 2:
                continue
            elif i == 3:
                limit = limits["m1"]
            elif i == 4:
                limit = limits["m2"]

            target = find_target(arr, limit)
            if target == -1:
                return ""
            ans[i] = str(target)

        return "".join(ans)

    def largestTimeFromDigits_fail1(self, arr: List[int]) -> str:
        # 失敗原因
        # 無效情境, 假設錯握
        # 每次彈出最小值, 比較是否大於限制
        # 無法正確判斷是否為 有效時鐘數字

        # 容易忽略的地方
        # h2 會隨著 h1 的數值, 最大數值有所不同

        # hour1 [0,2]
        # hour2 [0,3] or [0,9]
        # minute1 [0,5]
        # minute2 [0,9]
        limits = {
            "h1": 2,
            "h2_small": 3, "h2_large": 9,
            "m1": 5,
            "m2": 9
        }

        h1 = -1
        temp = arr.copy()
        for i in range(3):
            limit = -1
            if i == 0:
                limit = limits["h1"]
            elif i == 1:
                limit = limits["h2_small"] if h1 == 2 else limits["h2_large"]
            elif i == 2:
                limit = limits["m1"]

            _min = min(temp)
            if _min > limit:
                return ""
            else:
                h1 = _min if i == 0 else -1
                temp.pop(temp.index(_min))

        def find_target(arr, limit) -> int:
            for v in range(limit, -1, -1):
                for i in range(len(arr)):
                    if v == arr[i]:
                        arr.pop(i)
                        return v

        ans = ["", "", ":", "", ""]
        for i in range(len(ans)):
            limit = -1
            if i == 0:
                limit = limits["h1"]
            elif i == 1:
                limit = limits["h2_small"] if ans[0] == "2" else limits["h2_large"]
            elif i == 2:
                continue
            elif i == 3:
                limit = limits["m1"]
            elif i == 4:
                limit = limits["m2"]

            ans[i] = str(find_target(arr, limit))

        return "".join(ans)


if __name__ == '__main__':
    print(Solution().largestTimeFromDigits_v2([1, 2, 3, 4]))
    print(Solution().largestTimeFromDigits_v2([0, 0, 4, 0]))
    print(Solution().largestTimeFromDigits_v2([5, 5, 5, 5]))
    print(Solution().largestTimeFromDigits_v2([4, 4, 4, 0]))
    print(Solution().largestTimeFromDigits_v2([1, 9, 6, 0]))
    print(Solution().largestTimeFromDigits_v2([2, 0, 6, 6]))
