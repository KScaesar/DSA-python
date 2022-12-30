import collections
from typing import List


class Solution:
    # https://leetcode.com/problems/course-schedule/
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: dict[int, list[int]] = collections.defaultdict(list)
        for c in prerequisites:
            _goal = c[0]
            _need = c[1]
            graph[_goal].append(_need)

        track = set()
        visited = [False] * numCourses

        def dfs_ok_finish(goal) -> bool:
            nonlocal track
            if goal in track:
                return False

            # 正確的檢查位置
            if visited[goal]:
                return True

            visited[goal] = True
            track.add(goal)
            for need in graph[goal]:
                print(f' goal={goal} need={need} tack={track}')

                # 不應該在這邊檢查 是否曾經尋訪, 否則無法檢查 cycle 是否發生
                # if visited[need]:
                #     continue

                if not dfs_ok_finish(need):
                    return False

            # del (track, goal)  # 錯誤語法, 這樣會一次刪除 track goal 兩個變數
            track.remove(goal)

            return True  # 沒有這句程式, 預設回傳 None, 同等 False

        for course in range(numCourses):
            print(f' course={course}')
            if not dfs_ok_finish(course):
                return False

        return True


if __name__ == '__main__':
    print(Solution().canFinish(2, [[1, 0], [0, 1]]))
    print(Solution().canFinish(2, [[1, 0]]))
